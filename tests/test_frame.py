import os
import sys
from fastapi.testclient import TestClient
import main
from main import app
import json

from services.full_service import post, get, delete

client = TestClient(app)

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


async def test_post():
    file = {'files': open('tests/example.jpg', 'rb')}
    response = client.post("/frames/", files=file)
    await post(file)
    fileName =

    assert response.status_code == 200


def test_get():
    responses = client.get('/frames/')
