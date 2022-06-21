import uvicorn
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db
import os
from services.minio_service import MINIO_CLIENT
from api import router

app = FastAPI()
app.include_router(router)

# to avoid csrftokenError
app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])


# To run locally
if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)
    found = MINIO_CLIENT.bucket_exists('data')
    if not found:
        MINIO_CLIENT.make_bucket('data')
    else:
        print('Bucket already exist')

