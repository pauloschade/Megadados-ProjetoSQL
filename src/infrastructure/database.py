import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

load_dotenv()

USER = os.getenv('USER_NAME')
PASSWD = os.getenv('PASSWD')
DBNAME =  os.getenv('DBNAME')
IP = os.getenv('IP')

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{USER}:{PASSWD}@{IP}/{DBNAME}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db_connection():
    db = scoped_session(SessionLocal)
    try:
        yield db
    finally:
        db.close()

def create_all():
    Base.metadata.create_all(engine)

def get_db():
    return  scoped_session(SessionLocal)
