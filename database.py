from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine=create_engine('sqlite:///root2.db', echo=True)

Base=declarative_base()
