
import os
import sys
from fastapi.testclient import TestClient
import main
from main import app

client = TestClient(app)

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_post_message():
    filename = 'example.jpg'

    with open(filename, 'rb') as f:

        response = client.post('/frames',
                               data=f,
                               headers={"Content-Type": "multipart/form-data"}
                               )
        assert response.status_code == 200

