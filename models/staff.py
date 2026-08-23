from __future__ import annotations
from sqlalchemy import column,Integer,ForeignKey,String,Boolean
from sqlalchemy.orm import mapped_column,Mapped,relationship
from database import Base
import uuid
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .department import Department



class Staff(Base):
    __tablename__ = "staff"
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
    position:Mapped[str] = mapped_column(
        String(30),
        unique=False,
        nullable=False
    )
    deptID:Mapped[str] = mapped_column(
            ForeignKey("departments.deptID"),
            nullable=False
        )
    department: Mapped["Department"] = relationship("Department", back_populates="staff")