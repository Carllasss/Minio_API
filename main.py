import uvicorn
from fastapi import FastAPI, UploadFile, File, Response, HTTPException
from fastapi_sqlalchemy import DBSessionMiddleware, db
from minio import Minio
from http.client import HTTPException
from schema import Inbox as In
from typing import List
from models import Frame as Frame
import uuid
import os
from dotenv import load_dotenv
load_dotenv('.env')


app = FastAPI()

ACCESS_KEY = os.environ.get('ACCESS_KEY')
SECRET_KEY = os.environ.get('SECRET_KEY')

MINIO_API_HOST = 'http://localhost:9000'

MINIO_CLIENT = Minio('localhost:9000',
                     access_key=ACCESS_KEY,
                     secret_key=SECRET_KEY,
                     secure=False)

save_path = './media/'
# to avoid csrftokenError
app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])


@app.get("/")
async def root():
    return {"message": "hello world"}

"""
@app.post('/frames/')
async def upload(files: List[UploadFile] = File()):
    req = uuid.uuid4()
    for file in files:
        try:
            content = await file.read()
            fileName = str(uuid.uuid4())
            completeName = os.path.join(save_path, fileName+'.png')
            with open(completeName, 'wb') as f:
                f.write(content)
                db_frame = Frame(title=fileName, request=req)
                db.session.add(db_frame),
                db.session.commit()

        except Exception:
            return {"message": "There was an error uploading the file(s)"}
        finally:
            await file.close()

    return {"message": f"Successfuly uploaded {[file.filename for file in files]}"}
"""

@app.post('/frames/')
async def upload(files: List[UploadFile] = File()):
    if len(files) < 15:
        req = uuid.uuid4()
        for file in files:
            try:

                fileName = str(uuid.uuid4())
                MINIO_CLIENT.fput_object('data', fileName+'.png', file.file.fileno())
                db_frame = Frame(title=fileName, request=req)
                db.session.add(db_frame),
                db.session.commit()

            except Exception:
                return Exception

        return { "request_id" : req, 'files': [file.filename for file in files]}
    else:
        return {'error': f'Too many files. No more than 15 required.'}




@app.get('/frames/{request}')
async def frame(request: str):
    frames = db.session.query(Frame).filter(Frame.request == str(request))
    if not frames:
        raise HTTPException(status_code=404, detail="Frame not found")

    return frames

"""
@app.delete("/point/{point_id}")
async def delete_point(point_id: int):
    frame = db.session.get(Frame, point_id)
    if not frame:
        raise HTTPException(status_code=404, detail="Point not found")
    db.session.delete(frame)
    db.session.commit()
    return {"ok": True}

"""
# To run locally
if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)
    found = MINIO_CLIENT.bucket_exists('data')
    if not found:
        MINIO_CLIENT.make_bucket('data')
    else:
        print('Bucket already exist')
"""
db_point = Frame(title=uuid.uuid4(), request=req)
                db.session.add(db_point),
                db.session.commit()
                """