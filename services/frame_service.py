from datetime import datetime

from fastapi import HTTPException
from uuid import uuid4

from services.db_service import DbClient

from services.minio_service import MinioClient

minio_client = MinioClient()
db_client = DbClient()


def post(files):
    request_id = uuid4()
    new_files_names = []
    date = datetime.now().strftime('%Y.%m.%d')
    for file in files:
        try:
            file_name = (str(uuid4()) + '.jpg')
            new_files_names.append(file_name)
            minio_client.minio_post(file_name, file, date)
            db_client.db_post(file_name, request_id)

        except Exception:
            return Exception

    return {"request_id": request_id, 'files': [new_files_names[i-1] for i in range(len(new_files_names))]}


def get(request_id):
    frames = db_client.db_get_by_request_id(request_id)

    data = [{'id': frame.id} for frame in frames]
    if data == []:
        raise HTTPException(status_code=404, detail="Frame not found")

    return frames


def delete(request_id):
    frames = db_client.db_get_by_request_id(request_id).all()
    data = [{'created_at': frame.created_at} for frame in frames]
    if data == []:
        raise HTTPException(status_code=404, detail="Frame not found")
    date = (data[0]['created_at']).strftime('%Y.%m.%d')
    for frame in frames:
        minio_client.minio_delete(frame, date)
        db_client.db_delete(frame)
    return 204
