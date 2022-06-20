from pydantic import BaseModel



class Inbox(BaseModel):
    request: str
    title: str
    time_created: str