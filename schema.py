from pydantic import BaseModel


class GetFrame(BaseModel):
    title: str
    created_at: str
