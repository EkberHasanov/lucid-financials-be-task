from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.post import Post
from app.schemas.post import PostCreate


class PostRepository:


    def create(self, db: Session, post_create: PostCreate, user_id: int) -> Post:
        db_post = Post(
            text=post_create.text,
            user_id=user_id
        )
        db.add(db_post)
        db.commit()
        db.refresh(db_post)
        return db_post


    def get_by_id(self, db: Session, post_id: int) -> Optional[Post]:
        return db.query(Post).filter(Post.id == post_id).first()

    
    def get_user_posts(self, db: Session, user_id: int) -> List[Post]:
        return db.query(Post).filter(Post.user_id == user_id).all()
    

    def delete(self, db: Session, post_id: int, user_id: int) -> bool:
        post = db.query(Post).filter(
            Post.id == post_id,
            Post.user_id == user_id
        ).first()
        
        if not post:
            return False
            
        db.delete(post)
        db.commit()
        return True
