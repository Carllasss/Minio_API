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

    def minio_post(self, file_name, file):
        self.client.fput_object('data', file_name, file.file.fileno())

    def minio_delete(self, file_name):
        self.client.remove_object('data', file_name.title)

    def obj_exist(self, fileName):

        response = self.client.get_object('data', fileName)
        return response
