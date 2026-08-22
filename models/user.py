from __future__ import annotations
from sqlalchemy import column,Integer,ForeignKey,String,Boolean
from sqlalchemy.orm import mapped_column,Mapped,DeclarativeBase
from database import Base
import uuid

class User(Base):
    __tablename__ = "users"
    userID:Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda:str(uuid.uuid4()))
    email:Mapped[str] = mapped_column(
        String(30),
        unique=True,
        nullable=False
    )
    hashed_password:Mapped[str] = mapped_column(
        String(40),
        unique=False,
        nullable=False
    )
    role:Mapped[str] = mapped_column(
        String(10),
        unique=False,
        nullable=False
    )
    is_active:Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False

    )
