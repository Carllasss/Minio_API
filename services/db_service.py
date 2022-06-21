from models import Frame
from fastapi_sqlalchemy import db
from fastapi import HTTPException, Response
from uuid import uuid4


def db_post(fileName,request_id):

    db_frame = Frame(title=fileName, request=request_id)
    db.session.add(db_frame),
    db.session.commit()
    return Response('db posted too')


async def db_get_by_request_id(request_id):
    frames = db.session.query(Frame).filter(Frame.request == str(request_id))
    if not frames:
        raise HTTPException(status_code=404, detail="Frame not found")

    return [{'file': frame.title + '.png', 'time_created': frame.time_created} for frame in frames]


async def db_delete(frame):

    db.session.delete(frame)
    db.session.commit()

    return ('deleted')
