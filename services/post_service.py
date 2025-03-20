from typing import List
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repositories.post_repository import PostRepository
from app.repositories.user_repository import UserRepository
from app.schemas.post import PostCreate, Post
from app.utils.cache import cache

class PostService:


    def __init__(self):
        self.post_repository = PostRepository()
        self.user_repository = UserRepository()

    
    def create_post(self, db: Session, post_create: PostCreate, user_id: int) -> Post:
        user = self.user_repository.get_by_id(db, user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        
        db_post = self.post_repository.create(db, post_create, user_id)
        
        cache_key = f"user_posts_{user_id}"
        cache.delete(cache_key)
        
        return Post.from_orm(db_post)


    def get_user_posts(self, db: Session, user_id: int) -> List[Post]:
        user = self.user_repository.get_by_id(db, user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        
        cache_key = f"user_posts_{user_id}"
        cached_posts = cache.get(cache_key)
        if cached_posts:
            return cached_posts
        
        db_posts = self.post_repository.get_user_posts(db, user_id)
        posts = [Post.from_orm(post) for post in db_posts]
        
        cache.set(cache_key, posts)
        
        return posts
    

    def delete_post(self, db: Session, post_id: int, user_id: int) -> bool:
        result = self.post_repository.delete(db, post_id, user_id)
        if not result:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Post not found or not owned by user"
            )
        
        cache_key = f"user_posts_{user_id}"
        cache.delete(cache_key)
        
        return True
