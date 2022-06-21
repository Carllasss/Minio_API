from fastapi import APIRouter, UploadFile, File
from services.full_service import post, get, delete
from typing import List
from fastapi.responses import JSONResponse, Response


router = APIRouter(
    prefix="/frames",
    tags=["Frames"],
    responses={404: {"description": "Not found"}},
)


@router.post('/')
async def upload_frame(files: List[UploadFile] = File()):
    if len(files) > 15:
        return {'error': f'Too many files. No more than 15 required.'}
    result = post(files)
    return result


@router.get('/{request_id}')
async def get_frame(request_id: str):
    result = get(request_id)
    return result


@router.delete("/{request_id}")
async def delete_frame(request_id: str):
    result = delete(request_id)
    return Response(status_code=204)



