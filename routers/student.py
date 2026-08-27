from fastapi import APIRouter,Depends,Query
from database import get_db
from schemas import StudentUpdate,StudentRead,StudentCreate
from sqlalchemy.orm import Session
from services.student import read_student,list_students,create_student,update_student,delete_student



router = APIRouter(
    prefix="/students",
    tags=["students"])

@router.get("/{userID}",response_model = StudentRead)
def getstudent(userID:str,db:Session = Depends(get_db)):
    return read_student(db,userID)

@router.get("/",response_model=list[StudentRead])
def liststudents(
    db:Session = Depends(get_db),
    skip:int = Query(0,ge=0),
    limit:int = Query(10,ge=1,le=100)):
    return list_students(db,skip = skip,limit = limit)

@router.post("/",response_model=StudentCreate,status_code=201)
def createstudent(student_data:StudentCreate,db:Session = Depends(get_db)):
    return create_student(db,student_data)

@router.patch("/{userID}",response_model=StudentUpdate)
def updatestudent(studentID:int,student_data:StudentUpdate,db:Session = Depends(get_db)):
    return update_student(db,studentID,student_data)

@router.delete("/{userID}",status_code=204)
def deletestudent(studentID:int,db:Session = Depends(get_db)):
    return delete_student(db,studentID)