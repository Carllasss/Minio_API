import os
from dotenv import load_dotenv

load_dotenv('.env')

DATABASE_URL = os.environ.get('DATABASE_URL', "postgresql://postgres:12345@localhost/testdb")

MINIO_HOST = os.environ.get('MINIO_HOST')
ACCESS_KEY = os.environ.get('ACCESS_KEY')
SECRET_KEY = os.environ.get('SECRET_KEY')
