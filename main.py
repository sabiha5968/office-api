from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
from database import sessionLocal
from models import Employee, Department
from validators import EmployeeRequest, EmployeeResponse, DepartmentRequest, DepartmentResponse
from uuid import uuid4

app=FastAPI(debug=True)

def get_db():
    db = sessionLocal()
    try:
        yield db
    except:
        db.close()

#--------------employee tables--------

@app.get("/employee/", response_model=List[EmployeeResponse])
async def read(db : Session = Depends(get_db)):
    employee = db.query(Employee).all()
    return employee

@app.post("/employee/", response_model = EmployeeResponse)
async def create(
        employee: EmployeeRequest,
        db : Session = Depends(get_db),
):
    employee_dict = employee.dict()
    result = db.query(Employee).where(Employee.email_id == employee_dict["email_id"]).first()
    # print(result.__dict__)
    if result:
        raise HTTPException(
            status_code=422,
            detail="email already exists",
    )
    emp = Employee(**employee_dict)
    print(emp.__dict__)
    db.add(emp)
    db.commit()
    db.refresh(emp)
    print(emp)

    return emp

@app.get("/employee/{id}/",response_model = EmployeeResponse)
async def read_by_name(
        id=str,
        db : Session = Depends(get_db)
):
    result=db.query(Employee).where(Employee.id == id).first()
    if not result:
        raise HTTPException(
            status_code = 404,
            detail = "details not found",
        )
    return result

@app.patch("/employee/{id}/",response_model = EmployeeResponse)
async def update(
        id: str,
        employee:EmployeeRequest,
        db : Session = Depends(get_db)
):
    result = db.query( Employee ).where(Employee.id==id).first()

    if not result:
        raise HTTPException(status_code = 404,detail = "details not found")
    current_dict=employee.dict(exclude_unset=True)
    for key, values in current_dict.items():
        setattr(result,key,values)
    db.add(result)
    db.commit()
    db.refresh(result)
    return result

@app.delete("/employee/{id}/")
async def delete(
        id : str,
        db : Session = Depends(get_db),
):
    result = db.query(Employee).where(Employee.id == id).first()
    if not result:
        raise HTTPException(status_code = 404,detail = "details not found")
    db.delete(result)
    db.commit()
    db.close()
    return "Success"

#---------------------Department apis-----------

@app.get('/department/',response_model=List[DepartmentResponse])
async def read_all(
        db : Session = Depends(get_db)
):
    object=db.query(Department).all()

    return object


@app.get("/department/{id}/", response_model=DepartmentResponse)
async def read_by_id(
        id : str,
        db : Session = Depends(get_db),
):
    object = db.query(Department).where(Department.id == id).first()
    if not object:
        raise HTTPException(status_code=404, detail="data not found")
    return object


@app.post("/department/", response_model = DepartmentResponse)
async def create(
        department: DepartmentRequest,
        db : Session = Depends(get_db),
):
    department_dict = department.dict()
    result = db.query(Department).where(Department.name == department_dict["name"]).first()
    if result:
        raise HTTPException(status_code = 422, detail="department already exists" )
    de = Department(**department_dict)
    db.add(de)
    db.commit()
    db.refresh(de)
    print(de.__dict__)
    return de


@app.patch("/department/{id}/", response_model = DepartmentResponse)
async def update(
        id:str,
        department : DepartmentRequest,
        db : Session = Depends(get_db),
):

    object = db.query( Department ).where( Department.id==id ).first()
    if not object:
        raise HTTPException( status_code = 404,detail = "data not found")
    current_dict = department.dict( exclude_unset=True)
    for key,values in current_dict.items():
        setattr( object, key, values )
    db.add( object )
    db.commit()
    db.refresh( object )
    return object


@app.delete("/department/{id}/")
async def delete(
        id: str,
        db : Session = Depends(get_db),
):
    object = db.query( Department ).where( Department.id==id ).first()
    if not object:
        raise HTTPException( status_code = 404, detail = "data not found" )
    db.delete(object)
    db.commit()
    return {"ok": "True"}


