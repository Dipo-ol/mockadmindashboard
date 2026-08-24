from pydantic import BaseModel

class StudentCreate(BaseModel):
    firstname:str
    lastname:str
    matNo:str
    level:str
    department:str

class StudentRead(BaseModel):
    userID:str
    firstname:str
    lastname:str
    matNo:str
    level:str
    department:str
    model_config = {
        "from_attributes" : True
    }

class StudentUpdate(BaseModel):
    firstname:str
    lastname:str
    matNo:str
    level:str
    department:str