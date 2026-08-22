from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,DeclarativeBase
import sqlite3

connection = sqlite3.connect('mockdash.db')
connection.close()
DATABASE_URL = "sqlite+pysqlite:///mockdash.db"
engine = create_engine(DATABASE_URL,echo=True)

SessionLocal = sessionmaker(
    autoflush=False,
    bind=engine,
    autocommit=False
)

def get_db():
    db = SessionLocal
    try:
        yield db
    finally:
        db.close()

class Base(DeclarativeBase):
    pass
