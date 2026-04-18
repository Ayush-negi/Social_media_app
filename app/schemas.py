from pydantic import BaseModel

from datetime import datetime

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    """Used for POST /posts — all fields required unless defaulted in Base."""
    pass


class Post(PostBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True