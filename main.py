import uvicorn
from fastapi import FastAPI, UploadFile, File, Response, HTTPException
from fastapi_sqlalchemy import DBSessionMiddleware, db
from minio import Minio
from http.client import HTTPException
from typing import List
from models import Frame as Frame
import uuid
import os
from services.full_service import post
from services.minio_service import MINIO_CLIENT



app = FastAPI()

# to avoid csrftokenError
app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])


@app.get("/")
async def root():
    return {"message": "hello world"}


@app.post('/frames/')
async def upload(files: List[UploadFile] = File()):
    if len(files) > 15:
        return {'error': f'Too many files. No more than 15 required.'}
    result = post(files)
    return result

"""
@app.get('/frames/{request_id}')
async def frame(request_id: str):
    result = db_get_by_request_id(request_id)

    return result


@app.delete("/frames/{request_id}")
async def delete_frame(request_id: str):
    frames = db.session.query(Frame).filter(Frame.request == str(request_id))
    if not frames:
        raise HTTPException(status_code=404, detail="Frame not found")
    for frame in frames:
        minio_delete(frame)
        result = db_delete(frame)
    return result

"""



# To run locally
if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)
    found = MINIO_CLIENT.bucket_exists('data')
    if not found:
        MINIO_CLIENT.make_bucket('data')
    else:
        print('Bucket already exist')

