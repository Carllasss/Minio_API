from pydantic import BaseModel



class Inbox(BaseModel):
    request_id: str
    title: str
    created_at: str