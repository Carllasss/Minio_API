from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import config
from models import Frame
from fastapi import Response


class DbClient:
    def __init__(self):
        engine = create_engine(config.DATABASE_URL)
        engine.connect()
        session = sessionmaker(bind=engine)
        self.session = session()

    def db_post(self, fileName, request_id):
        db_frame = Frame(title=fileName, request=request_id)
        self.session.add(db_frame),
        self.session.commit()
        return Response('db posted too')

    def db_get_by_request_id(self, request_id):
        frames = self.session.query(Frame).filter(Frame.request == str(request_id))

        return frames

    def db_delete(self, frame):
        self.session.delete(frame)
        self.session.commit()
        return 'deleted'
