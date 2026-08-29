from fastapi import Depends,HTTPException
from sqlalchemy import String,select
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound,SQLAlchemyError 
from database import get_db
from schemas.user import UserCreate,UserRead,UserUpdate,roleUpdate,passwordUpdate
from models.user import User
from pydantic import EmailStr
from security.password import hash_password







def get_user_by_id(db:Session,userID:str):
    try:
        result = db.get(User,userID)
        return result
    except NoResultFound:
        raise HTTPException(status_code=404,detail="cannot retrieve user")
    

def get_user_by_email(db:Session,email:EmailStr):
        smnt = select(User).where(User.email == email)
        result = db.execute(smnt).scalar_one_or_none()
        if result is None:
            raise HTTPException(status_code=404,detail="cannot retrieve user")
        else:
            return result
    
def list_users(db:Session,skip:int,limit:int):
    smnt = select(User).offset(skip).limit(limit)
    result = db.execute(smnt).scalars().all()
    return result
    
def create_user(db:Session,user_data:UserCreate):
    hashed_password = hash_password(user_data.password)

    existing_user = db.execute(select(User).where(User.email == user_data.email))
    if existing_user.scalar_one_or_none() is None:
        user = User(
            email = user_data.email,
            password = hashed_password,
            role = user_data.role
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    else:
        raise HTTPException(status_code=409,detail="user already exists")
    
    
def update_user(db:Session,userID:str,user_data:UserUpdate):
    user = db.get(User,userID)
    if user is None:
        raise HTTPException(status_code=404,detail="user not found")
    update_data = user_data.model_dump()
    for field,data in update_data.items():
        setattr(user,field,data)
    db.commit()
    db.refresh(user)
    return user


def delete_user(db:Session,userID:str):
    user = db.get(User,userID)
    if user is None:
        raise HTTPException(status_code=404,detail="user not found")
    db.delete(user)
    db.commit()


def deactivate_user(db,userID):
    user = db.get(User,userID)
    if user is None:
        raise HTTPException(status_code=404,detail="user not found")
    user.is_active = False
    db.commit()
    db.refresh(user)
