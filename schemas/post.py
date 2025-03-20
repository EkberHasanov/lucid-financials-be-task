from datetime import datetime
from pydantic import BaseModel, Field, validator


class PostBase(BaseModel):
    text: str = Field(
        ..., 
        min_length=1, 
        max_length=1000000,
        description="Post content",
        example="This is my first post!"
    )


    @validator('text')
    def validate_text_size(cls, v):
        if len(v.encode('utf-8')) > 1024 * 1024:
            raise ValueError('Post text exceeds 1MB size limit')
        return v


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    created_at: datetime


    class Config:
        orm_mode = True


class PostDelete(BaseModel):
    post_id: int = Field(..., description="ID of post to delete", example=1)
