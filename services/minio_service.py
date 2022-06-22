from fastapi import Response
from minio import Minio
import config


class MinioClient:
    def __init__(self):
        self.client = Minio(config.MINIO_HOST,
                            access_key=config.ACCESS_KEY,
                            secret_key=config.SECRET_KEY,
                            secure=False)
        found = self.client.bucket_exists('data')
        if not found:
            self.client.make_bucket('data')
        else:
            print('Bucket already exist')

    def minio_post(self, fileName, file):
        self.client.fput_object('data', fileName, file.file.fileno())
        return Response('posted')

    def minio_delete(self, fileName):
        self.client.remove_object('data', fileName.title)
        return ('deleted')
