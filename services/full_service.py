from datetime import datetime
from fastapi import HTTPException, Response
from uuid import uuid4
from services.minio_service import minio_delete, minio_post
from services.db_service import db_post, db_delete, db_get_by_request_id
import os


def post(files):
    for file in files:
        if os.path.splitext(file.filename)[1] != '.jpg':
            raise HTTPException(status_code=400, detail='Wrong file extension(' + file.filename + '). Only .jpg is allowed')
    request_id = uuid4()
    for file in files:

        try:
            fileName = (str(uuid4())+'.jpg')
            result = minio_post(fileName, file)
            result1 = db_post(fileName, request_id)

        except Exception:
            return Exception

    return {"request_id": request_id, 'files': [file.filename for file in files]}


def get(request_id):
    frames = db_get_by_request_id(request_id)
    return [{'file': frame.title + '.png', 'created_at': datetime.strftime(frame.created_at, "%d.%m.%Y, %H:%M:%S")} for frame in frames]


def delete(request_id):
    frames = db_get_by_request_id(request_id)

    for frame in frames:
        result = minio_delete(frame)
        result1 = db_delete(frame)
    return 200


