from fastapi import Response
from minio import Minio
import config


MINIO_CLIENT = Minio(config.MINIO_HOST,
                     access_key=config.ACCESS_KEY,
                     secret_key=config.SECRET_KEY,
                     secure=False)


def minio_post(fileName, file):
    MINIO_CLIENT.fput_object('data', fileName, file.file.fileno())
    return Response('posted')


def minio_delete(fileName):
    MINIO_CLIENT.remove_object('data', fileName.title)
    return ('deleted')