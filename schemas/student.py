from pydantic import BaseModel

class StudentCreate(BaseModel):
    firstname:str
    lastname:str
    matNo:str
    level:str

class StudentRead(BaseModel):
    userID:str
    firstname:str
    lastname:str
    matNo:str
    level:str

class StudentUpdate(BaseModel):
    firstname:str
    lastname:str
    matNo:str
    level:str