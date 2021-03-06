from sqlalchemy.sql import func
from sqlalchemy import Column, DateTime, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Frame(Base):
    __tablename__ = 'inbox'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    request = Column(String)
    title = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
