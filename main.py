import uvicorn
from fastapi import FastAPI, APIRouter
from fastapi_sqlalchemy import DBSessionMiddleware
import os
import databases
from endpoints import frame


database = databases.Database()
router = APIRouter()
router.include_router(frame.router)

app = FastAPI()
app.include_router(router)

# to avoid csrftokenError
app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])

@app.on_event('startup'):
async def startup():
    await data


# To run locally
if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)
