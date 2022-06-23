from datetime import datetime

from fastapi import APIRouter, UploadFile, File, HTTPException
from services.frame_service import post, get, delete
from typing import List
from fastapi.responses import Response


router = APIRouter(
    prefix="/frames",
    tags=["Frames"],
    responses={404: {"description": "Not found"}},
)


@router.post('/')
async def upload_frame(files: List[UploadFile] = File()):
    if len(files) > 15:
        return {'error': f'Too many files. No more than 15 required.'}
    for file in files:
        if not file.filename.endswith('.jpg'):
            raise HTTPException(status_code=400,
                                detail='Wrong file extension(' + file.filename + '). Only .jpg is allowed')

    return post(files)



@router.get('/{request_id}')
async def get_frame(request_id: str):
    result = get(request_id)
    return [{'file': frame.title, 'created_at': datetime.strftime(frame.created_at, "%d.%m.%Y, %H:%M:%S")} for
            frame in result]


@router.delete("/{request_id}")
async def delete_frame(request_id: str):
    delete(request_id)
    return Response(status_code=204)
