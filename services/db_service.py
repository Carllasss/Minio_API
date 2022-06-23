from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import config
from models.frame_model import Frame
from fastapi import HTTPException


class DbClient:
    def __init__(self):
        engine = create_engine(config.DATABASE_URL)
        engine.connect()

        session = sessionmaker(bind=engine)
        self.session = session()

    def db_post(self, file_name, request_id):
        db_frame = Frame(title=file_name, request=request_id)
        self.session.add(db_frame),
        self.session.commit()

    def db_get_by_request_id(self, request_id):
        frames = self.session.query(Frame).filter(Frame.request == str(request_id))

        if not frames:
            raise HTTPException(status_code=404, detail="Frame not found")

        return frames

    def db_delete(self, frame):
        self.session.delete(frame)
        self.session.commit()

