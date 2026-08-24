from pydantic import BaseModel

class LecturerCreate(BaseModel):
    firstname:str
    lastname:str
    staffID:str
    rank:str
    department:str

class LecturerRead(BaseModel):
    userID:str
    firstname:str
    lastname:str
    staffID:str
    rank:str
    department:str
    model_config = {
        "from_attributes" : True
    }

class LecturerUpdate(BaseModel):
    firstname:str
    lastname:str
    staffID:str
    rank:str
    department:str