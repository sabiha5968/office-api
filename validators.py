from pydantic import BaseModel, root_validator,validate_email


class EmployeeRequest(BaseModel):
    name : str
    email_id : str
    address : str
    department : str
    salary : float
    head : bool

    @root_validator
    def validate_email_field(cls,values):
        em=values.get("email_id")
        if em:
            validate_email(em)
        return values

    class Config:
        orm_mode=True

class EmployeeResponse(BaseModel):
    id:str
    name:str
    email_id:str
    address:str
    department:str
    salary:float
    head:bool

    class Config:
        orm_mode=True

class DepartmentRequest(BaseModel):
    name:str

    class Config:
        orm_mode=True

class DepartmentResponse(BaseModel):
    id:str
    name:str

    class Config:
        orm_mode=True
