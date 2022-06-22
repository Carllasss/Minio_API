import os
import sys
import psycopg2
from fastapi import Depends
from fastapi_sqlalchemy import db
from fastapi.testclient import TestClient
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, Session

import main
import json

from models import Base
from services.full_service import get
import pytest

from services.full_service import post, get, delete

client = TestClient(main.app)

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

DATABASE_URL = 'postgresql://postgres:12345@localhost/testdb'
engine = create_engine(
    DATABASE_URL
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()





def test_post():
    file = {'files': open('tests/example.jpg', 'rb')}
    response = client.post("/frames/", files=file)
    data = response.json()
    assert (data['request_id']) is not None
    assert response.status_code == 200


# def test_get():
#     responses = client.get('/frames/')

