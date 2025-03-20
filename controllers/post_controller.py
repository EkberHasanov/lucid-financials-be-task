from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.models.database import get_db
from app.schemas.post import PostCreate, Post, PostDelete
from app.services.post_service import PostService
from app.dependencies import get_current_user_id

router = APIRouter(tags=["posts"])

post_service = PostService()


@router.post("/posts", response_model=Post, status_code=status.HTTP_201_CREATED)
async def add_post(
    post_create: PostCreate,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    return post_service.create_post(db, post_create, user_id)


@router.get("/posts", response_model=List[Post])
async def get_posts(
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    return post_service.get_user_posts(db, user_id)


@router.delete("/posts/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(
    post_id: int,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    post_service.delete_post(db, post_id, user_id)
    return None
