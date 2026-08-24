from pydantic import BaseModel

class DeptCreate(BaseModel):
    deptName:str

class DeptRead(BaseModel):
    deptID:str
    deptName:str
    model_config = {
        "from_attributes":True
    }

class DeptUpdate(BaseModel):
    deptName:str