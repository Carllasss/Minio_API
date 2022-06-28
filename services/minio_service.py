from minio import Minio
import config
import datetime


class MinioClient:
    def __init__(self):
        self.client = Minio(config.MINIO_HOST,
                            access_key=config.ACCESS_KEY,
                            secret_key=config.SECRET_KEY,
                            secure=False)

    def minio_post(self, file_name, file, date):
        found = self.client.bucket_exists(date)
        if not found:
            self.client.make_bucket(date)
        self.client.fput_object(date, file_name, file.file.fileno())

    def minio_delete(self, file_name, date):
        self.client.remove_object(date, file_name.title)

    def obj_exist(self, fileName):
        response = self.client.get_object('data', fileName)
        return response
