from datetime import datetime
from fastapi import HTTPException
from uuid import uuid4

from services.db_service import DbClient
import os

from services.minio_service import MinioClient

minio_client = MinioClient()
db_client = DbClient()


def post(files):
    for file in files:
        if os.path.splitext(file.filename)[1] != '.jpg':
            raise HTTPException(status_code=400,
                                detail='Wrong file extension(' + file.filename + '). Only .jpg is allowed')
    request_id = uuid4()
    for file in files:

        try:
            fileName = (str(uuid4()) + '.jpg')
            result = minio_client.minio_post(fileName, file)
            result1 = db_client.db_post(fileName, request_id)

        except Exception:
            return {'error': 'somethings gone wrong'}

    return {"request_id": request_id, 'files': [file.filename for file in files]}


def get(request_id):
    frames = db_client.db_get_by_request_id(request_id)
    data = [{'id': frame.id} for frame in frames]
    if data == []:
        raise HTTPException(status_code=404, detail="Frame not found")
    return [{'file': frame.title, 'created_at': datetime.strftime(frame.created_at, "%d.%m.%Y, %H:%M:%S")} for
            frame in frames]


def delete(request_id):
    frames = db_client.db_get_by_request_id(request_id).all()
    data = [{'id': frame.id} for frame in frames]
    if data == []:
        raise HTTPException(status_code=404, detail="Frame not found")
    for frame in frames:
        result = minio_client.minio_delete(frame)
        result1 = db_client.db_delete(frame)
    return 204
