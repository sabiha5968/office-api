import os
import urllib

from sqlalchemy import create_engine
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


host_server = os.environ.get('host_server', 'localhost')
db_server_port = urllib.parse.quote_plus(str(os.environ.get('db_server_port', '5432')))
database_name = os.environ.get('database_name', 'office1')
db_username = urllib.parse.quote_plus(str(os.environ.get('db_username', 'sabihanaaz')))
db_password = urllib.parse.quote_plus(str(os.environ.get('db_password', 'naaz@5968')))
ssl_mode = urllib.parse.quote_plus(str(os.environ.get('ssl_mode','prefer')))
DATABASE_URL = 'postgresql://{}:{}@{}:{}/{}?sslmode={}'.format(db_username, db_password, host_server, db_server_port, database_name, ssl_mode)

engine=create_engine(DATABASE_URL, echo=True)

sessionLocal= sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base=declarative_base()



3
#
# {
#     "name" : "shiba",
#     "email_id": "we@exmaple.com",
#     "address": "gsfd",
#     "department": "35070393-0d73-4f8f-9b80-9e9cc33a0cc1",
#     "salary": 100,
#     "head": true,
#     "phone_number":"1231231231"
#
# }
