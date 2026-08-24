from pydantic import BaseModel,EmailStr,Field

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)
    role: str

class UserRead(BaseModel):
    userID: str
    email: EmailStr
    role: str

class UserUpdate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)
    role: str