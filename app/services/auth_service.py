from datetime import timedelta
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate
from app.schemas.token import Token
from app.utils.auth import create_access_token
from app.config import settings

class AuthService:


    def __init__(self):
        self.user_repository = UserRepository()
    

    def signup(self, db: Session, user_create: UserCreate) -> Token:
        db_user = self.user_repository.get_by_email(db, user_create.email)
        if db_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
        user = self.user_repository.create(db, user_create)
        access_token = create_access_token(
            data={"user_id": user.id},
            expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        )
        
        return Token(access_token=access_token, token_type="bearer")
    

    def login(self, db: Session, email: str, password: str) -> Token:
        user = self.user_repository.authenticate(db, email, password)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        access_token = create_access_token(
            data={"user_id": user.id},
            expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        )
        
        return Token(access_token=access_token, token_type="bearer")
