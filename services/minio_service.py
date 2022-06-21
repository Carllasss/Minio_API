
from fastapi import Response

from minio import Minio
import os
from dotenv import load_dotenv


load_dotenv('.env')
ACCESS_KEY = os.environ.get('ACCESS_KEY')
SECRET_KEY = os.environ.get('SECRET_KEY')

MINIO_API_HOST = 'http://localhost:9000'

MINIO_CLIENT = Minio('localhost:9000',
                     access_key=ACCESS_KEY,
                     secret_key=SECRET_KEY,
                     secure=False)


def minio_post(fileName, file):
    MINIO_CLIENT.fput_object('data', fileName + '.png', file.file.fileno())
    return Response('posted')


def minio_delete(fileName):
    MINIO_CLIENT.remove_object('data', (fileName.title + '.png'))
    return fileName + ' deleted'