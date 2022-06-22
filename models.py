import datetime


from sqlalchemy import Column, DateTime, String, Integer, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData()

frame_table = Table(
    'inbox',
    metadata,
    Column('id', Integer, primary_key=True, unique=True, autoincrement=True),
    Column('request', String),
    Column('title', String),
    Column('created_at', DateTime(timezone=True), server_default=datetime.datetime.now().isoformat(" ", "seconds"))
)
