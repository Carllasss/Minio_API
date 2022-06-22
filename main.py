import uvicorn
from fastapi import FastAPI, APIRouter
from fastapi_sqlalchemy import DBSessionMiddleware
import os

from endpoints import frame

router = APIRouter()
router.include_router(frame.router)

app = FastAPI()
app.include_router(router)

# to avoid csrftokenError
app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])

# To run locally
if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)
