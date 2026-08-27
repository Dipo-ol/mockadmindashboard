from __future__ import annotations
from sqlalchemy import column,Integer,ForeignKey,String,Boolean
from sqlalchemy.orm import mapped_column,Mapped,DeclarativeBase,relationship
from database import Base
import uuid
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .student import Student
    from .lecturer import Lecturer
    from .staff import Staff

class Department(Base):      #creates a model for the department table in the database
    __tablename__ = "departments"
    deptID:Mapped[str] = mapped_column(
        String(40),
        primary_key=True,
        default=lambda:str(uuid.uuid4()))
    deptName:Mapped[str] = mapped_column(String(36))
    students: Mapped[list["Student"]] = relationship("Student", back_populates="department")
    lecturers:Mapped[list["Lecturer"]] = relationship("Lecturer", back_populates="department")
    staff:Mapped[list["Staff"]] = relationship("Staff", back_populates="department")
#creates a relationship between department and students