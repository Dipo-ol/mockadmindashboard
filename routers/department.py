from fastapi import APIRouter,HTTPException,Depends,Query
from sqlalchemy.orm import Session
from database import get_db
from services.department  import (create_dept,read_dept,read_depts,delete_dept,update_dept)
from schemas.department import (DeptCreate,DeptRead,DeptUpdate)


router = APIRouter(
    prefix="/departments",
    tags=["departments"]
)


@router.get("/{deptID}",response_model = DeptRead)
def getdepartment(deptID:str,db:Session = Depends(get_db)):
    return read_dept(db,deptID)

@router.get("/",response_model=list[DeptRead])
def listdepartments(
    db:Session = Depends(get_db),
    skip:int = Query(0,ge=0),
    limit:int = Query(10,ge=1,le=100)):
    return read_depts(db,skip = skip,limit = limit)

@router.post("/",response_model=DeptCreate,status_code=201)
def createdept(department_data:DeptCreate,db:Session = Depends(get_db)):
    return create_dept(db,department_data)

@router.patch("/{deptID}",response_model=DeptUpdate)
def updatedepartment(deptID:str,department_data:DeptUpdate,db:Session = Depends(get_db)):
    return update_dept(db,deptID,department_data)

@router.delete("/{deptID}",status_code=204)
def deletedepartment(deptID:str,db:Session = Depends(get_db)):
    return delete_dept(db,deptID)