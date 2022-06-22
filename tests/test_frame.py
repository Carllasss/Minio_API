import os
import sys

from fastapi_sqlalchemy import db
from fastapi.testclient import TestClient
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, Session

import main
import json
from services.full_service import get
import pytest

from services.full_service import post, get, delete

client = TestClient(main.app)

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@pytest.fixture(scope="session")
def engine():
    return create_engine("postgresql://localhost/test_database")


@pytest.fixture(scope="session")
def tables(engine):
    BaseModel.metadata.create_all(engine)
    yield
    BaseModel.metadata.drop_all(engine)


@pytest.fixture
def dbsession(engine, tables):
    """Returns an sqlalchemy session, and after the test tears down everything properly."""
    connection = engine.connect()
    # begin the nested transaction
    transaction = connection.begin()
    # use the connection with the already started transaction
    session = Session(bind=connection)

    yield session

    session.close()
    # roll back the broader transaction
    transaction.rollback()
    # put back the connection to the connection pool
    connection.close()


def test_post():
    file = {'files': open('tests/example.jpg', 'rb')}
    response = client.post("/frames/", files=file)
    data = response.json()
    assert (data['request_id']) is not None
    assert response.status_code == 200


# def test_get():
#     responses = client.get('/frames/')

