from __future__ import annotations
from sqlalchemy import column,Integer,ForeignKey,String,Boolean
from sqlalchemy.orm import mapped_column,Mapped,DeclarativeBase
from database import Base
import uuid

class Student(Base):
    userID:Mapped[str] = mapped_column(
        String(40),
        ForeignKey("users.userID"),
        primary_key=True
    )
    firstName:Mapped[str] = mapped_column(
        String(25),
        unique=False,
        nullable=False
    )
    lastName:Mapped[str] = mapped_column(
        String(30),
        unique=False,
        nullable=False
    )
    matNo:Mapped[str] = mapped_column(
        String(15),
        unique=True,
        nullable=True
    )
    level:Mapped[str] = mapped_column(
        String(3),
        nullable=False,
        unique=False
    )