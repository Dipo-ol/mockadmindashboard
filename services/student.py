from sqlalchemy import select,update
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError,NoResultFound,IntegrityError
from models import Student,Department
from schemas.student import StudentCreate,StudentUpdate,StudentRead
from fastapi import HTTPException

def create_student(db:Session,student_data:StudentCreate):
    try:
        result = db.execute(select(Student).where(Student.matNo == student_data.matNo))
        existingstudent = result.scalar_one_or_none()
        if existingstudent is None:

            student_dict = student_data.model_dump()
            department = db.execute(select(Department).where(Department.deptName == student_data.department)).scalar_one_or_none()
            if not department:
                raise HTTPException(status_code=404,detail= "Department not found")

    
            student_dict["dept_ID"] = department.deptID
            new_student = Student(**student_dict)
            db.add(new_student)
            db.commit()
            db.refresh(new_student)
            return new_student
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409,detail="student already exists")


def list_students(db:Session,skip:int,limit:int):
    try:
        stmt = select(Student).offset(skip).limit(limit)
        students = db.execute(stmt).scalars().all()
        return students
 
    except NoResultFound:
        raise HTTPException(status_code=404,detail="student not found")
             


def read_student(db:Session,userID:str):
    try:
        result = db.get(Student,userID)
        return result
    except NoResultFound:
        raise HTTPException(status_code=404,detail="student not found")


def update_student(db:Session,userID:int,student_data:StudentUpdate):
    result = db.get(Student,userID)
    try:
        if result is not None:
            update_data = student_data.model_dump(exclude_unset=True)
            for field,data in update_data.items():
                setattr(result,field,data)
            db.commit()
            db.refresh(result)
            return result
    except NoResultFound:
        raise HTTPException(status_code=404,detail="student not found")
    


def delete_student(db:Session,userID:int):
    result = db.get(Student,userID)
    if result is not None:
        db.delete(result)
        db.commit()
    else:
        raise HTTPException(status_code=404,detail="student not found")




    