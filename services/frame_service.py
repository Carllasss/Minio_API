from datetime import datetime
from fastapi import HTTPException
from uuid import uuid4

from services.db_service import DbClient

from services.minio_service import MinioClient

minio_client = MinioClient()
db_client = DbClient()


def post(files):
    request_id = uuid4()
    for file in files:

        try:
            file_name = (str(uuid4()) + '.jpg')
            minio_client.minio_post(file_name, file)
            db_client.db_post(file_name, request_id)

        except Exception:
            return {'error': 'somethings gone wrong'}

    return {"request_id": request_id, 'files': [file.filename for file in files]}


def get(request_id):
    frames = db_client.db_get_by_request_id(request_id)

    data = [{'id': frame.id} for frame in frames]
    if data == []:
        raise HTTPException(status_code=404, detail="Frame not found")

    return frames


def delete(request_id):
    frames = db_client.db_get_by_request_id(request_id).all()
    data = [{'id': frame.id} for frame in frames]
    if data == []:
        raise HTTPException(status_code=404, detail="Frame not found")
    for frame in frames:
        minio_client.minio_delete(frame)
        db_client.db_delete(frame)
    return 204
