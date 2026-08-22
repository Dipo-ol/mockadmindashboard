from __future__ import annotations
from sqlalchemy import column,Integer,ForeignKey,String,Boolean
from sqlalchemy.orm import mapped_column,Mapped,DeclarativeBase
from database import Base
import uuid