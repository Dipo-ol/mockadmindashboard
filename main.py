from fastapi import FastAPI
from database import Base,engine
from models import Student,Staff,Department,Lecturer

Base.metadata.create_all(bind=engine)
app = FastAPI()