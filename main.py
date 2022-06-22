from fastapi import FastAPI, HTTPException
from typing import List
from sqlalchemy.orm import Session
from database import engine
from models import Employee, Department, Department
from validators import EmployeeRequest, EmployeeResponse, DepartmentRequest, DepartmentResponse
from uuid import uuid4



app=FastAPI()

session = Session(bind=engine, expire_on_commit=False)



@app.get("/employee/", response_model=List[EmployeeResponse])
async def read():
    employee = session.query(Employee).all()
    return employee

@app.post("/employee/", response_model = EmployeeResponse)
async def create(employee: EmployeeRequest):
    emp = Employee(**employee.dict())
    emp.id = str(uuid4())
    session.add(emp)
    session.commit()
    session.refresh(emp)

    return emp





@app.get("/employee/{id}/",response_model = EmployeeResponse)
async def read_by_name(
        id=str,
):
    result=session.query(Employee).where(Employee.id == id).first()
    if not result:
        raise HTTPException(
            status_code = 404,
            detail = "details not found",
        )
    return result

@app.patch("/employee/{id}/",response_model = EmployeeResponse)
async def update(
        id: str,
        employee:EmployeeRequest
):
    result=session.query( Employee ).where(Employee.id==id).first()

    if not result:
        raise HTTPException(status_code = 404,detail = "details not found")
    current_dict=employee.dict(exclude_unset=True)
    for key, values in current_dict.items():
        setattr(result,key,values)
    session.add(result)
    session.commit()
    session.refresh(result)
    return result

@app.delete("/employee/{id}/")
async def delete(
        id : str
):
    result = session.query(Employee).where(Employee.id == id).first()
    if not result:
        raise HTTPException(status_code = 404,detail = "details not found")
    session.delete(result)
    session.commit()
    session.close()
    return "Success"

#---------------------Department apis-----------

@app.get('/department/',response_model=List[DepartmentResponse])
async def read_all():
    object=session.query(Department).all()
    return object


@app.get("/department/{id}/",response_model=DepartmentResponse)
async def read_by_id(id:str):
    object=session.query(Department).where(Department.id==id).first()
    if not object:
        raise HTTPException(status_code=404,detail="data not found")
    return object


@app.post("/department/", response_model = DepartmentResponse)
async def create(
        department: DepartmentRequest
):
    dep = Department( **department.dict())
    dep.id = str( uuid4() )
    session.add( dep )
    session.commit()
    session.refresh(dep)

    return dep


@app.patch("/department/{id}/", response_model = DepartmentResponse)
async def update(
        id:str,
        department : DepartmentRequest
):

    object = session.query( Department ).where( Department.id==id ).first()
    if not object:
        raise HTTPException( status_code = 404,detail = "data not found")
    current_dict = department.dict( exclude_unset=True)
    for key,values in current_dict.items():
        setattr( object, key, values )
    session.add( object )
    session.commit()
    session.refresh( object )
    return object


@app.delete("/department/{id}/")
async def delete(
        id: str
):
    object = session.query( Department ).where( Department.id==id ).first()
    if not object:
        raise HTTPException( status_code = 404, detail = "data not found" )
    session.delete(object)
    session.commit()
    return {"ok": "True"}


