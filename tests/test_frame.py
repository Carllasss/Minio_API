import os
import sys

from fastapi.testclient import TestClient
import main
from services.minio_service import MinioClient
from services.db_service import DbClient


client = TestClient(main.app)

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

min = MinioClient()
db = DbClient()


def test_post_get():
    file = {'files': open('tests/example.jpg', 'rb')}
    response = client.post("/frames/", files=file)
    data = response.json()
    frame = db.db_get_by_request_id(data['request_id']).all()
    assert frame != []
    assert response.status_code == 200


def test_post_bad_file():
    file = {'files': open('tests/example.PNG', 'rb')}
    response = client.post("/frames/", files=file)
    assert response.status_code == 400


def test_get():
    file = {'files': open('tests/example.jpg', 'rb')}
    help_response = client.post("/frames/", files=file)
    answer = help_response.json()['request_id']
    response = client.get('/frames/' + answer)
    assert response.status_code == 200
    assert response.json()[0]['file'] is not None


def test_get_bad_request():
    response = client.get('/frames/1')
    data = response.json()
    print(data)
    assert response.status_code == 404


def test_delete_bad_request():
    response = client.delete('/frames/1')
    assert response.status_code == 404


def test_delete():
    file = {'files': open('tests/example.jpg', 'rb')}
    help_response = client.post("/frames/", files=file)
    data = help_response.json()
    request_id = data['request_id']
    response = client.delete('/frames/' + request_id)
    assert response.status_code == 204
