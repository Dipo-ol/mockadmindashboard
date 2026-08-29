from pydantic import BaseModel,EmailStr,Field

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)
    role: str

class UserRead(BaseModel):
    userID: str
    email: EmailStr
    role: str
    is_active:str
    model_config = {
       "from_attributes":True
    }

class UserUpdate(BaseModel):
    email: EmailStr

class passwordUpdate(BaseModel):
    password: str =Field(min_length=8)

class roleUpdate(BaseModel):
    role:str