from sqlalchemy import select,update
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError,NoResultFound,IntegrityError
from models import Department
from schemas.department import DeptCreate,DeptRead,DeptUpdate
from fastapi import HTTPException


def create_dept(db:Session,department_data:DeptCreate):
    
    result = db.execute(select(Department).where(Department.deptName == department_data.deptName))
    if result.scalar_one_or_none() is None:
        department = Department(**department_data.model_dump())
        try:
            db.add(department) 
            db.commit()
            db.refresh(department)
            return department
        except IntegrityError:
            db.rollback()
            raise HTTPException(status_code=500,detail="could not create department")
    else:
        raise HTTPException(status_code=409,detail="department already exists")

        


def read_dept(db:Session,deptID:str):
    try:
        department = db.get(Department,deptID)
        if department is not None:
            return department
    except NoResultFound:
        raise HTTPException(status_code=404,detail="department not found")

def read_depts(db:Session,skip:int,limit:int):
    try:
        stmt = select(Department).offset(skip).limit(limit)
        departments = db.execute(stmt).scalars().all()

        if departments is not None:
            return departments
    except SQLAlchemyError:
        raise HTTPException(status_code=500,detail="internal sever error")
    

def update_dept(db:Session,deptID:str,department_data:DeptUpdate):
    try:
        result = db.get(Department,deptID)
        if result is not None:
            update_data = department_data.model_dump(exclude_unset=True)
            for field,data in update_data.items():
                setattr(result,field,data)
            db.commit()
            db.refresh(result)
            return result
        
    except NoResultFound:
        raise HTTPException(status_code=404,detail="department not found")
    except SQLAlchemyError:
        raise HTTPException(status_code=500,detail="unexpected server error")

def delete_dept(db:Session,deptID:str):
    result = db.get(Department,deptID)
    if result is not None:
        db.delete(result)
        db.commit()
    else:
        raise HTTPException(status_code=404,detail="department does not exist")

