from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class TimeRecord(Base):
    __tablename__ = "time_record"
    id = Column(Integer, primary_key=True, unique=True)
    session_name = Column(String)
    session_date = Column(DateTime)
    session_duration = Column(Integer)
