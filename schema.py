from pydantic import BaseModel



class Inbox(BaseModel):
    title: str
    created_at: str