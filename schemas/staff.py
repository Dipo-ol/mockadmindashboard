from pydantic import BaseModel

class StaffCreate(BaseModel):
    firstname:str
    lastname:str
    staffID:str
    position:str
    department:str

class StaffRead(BaseModel):
    firstname:str
    lastname:str
    staffID:str
    position:str
    department:str
    model_config = {
        "from_attributes" : True
    }

class StaffUpdate(BaseModel):
    firstname:str
    lastname:str
    staffID:str
    position:str
    department:str