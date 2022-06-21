from fastapi import APIRouter
from endpoints import frame

router = APIRouter()
router.include_router(frame.router)