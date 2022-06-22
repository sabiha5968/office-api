from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, CHAR
from sqlalchemy.orm import relationship
from database import Base, engine
from uuid import UUID

class Employee(Base):
    __tablename__="employee"
    id=Column(CHAR(32), primary_key=True)
    name=Column(String)
    address=Column(String)
    email_id=Column(String)
    department= Column(CHAR(32), ForeignKey("department.id"))
    salary=Column(Integer)
    head=Column(Boolean)




class Department(Base):
    __tablename__="department"
    id=Column(CHAR(32), primary_key=True)
    name=Column(String)

Base.metadata.create_all(engine)


