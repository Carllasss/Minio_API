from pydantic import BaseModel



class Inbox(BaseModel):
    request: str
    title: str
    created_at: str