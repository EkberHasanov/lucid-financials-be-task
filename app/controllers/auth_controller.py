from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.models.database import get_db
from app.schemas.user import UserCreate, UserLogin
from app.schemas.token import Token
from app.services.auth_service import AuthService

router = APIRouter(tags=["authentication"])

auth_service = AuthService()


@router.post("/signup", response_model=Token, status_code=status.HTTP_201_CREATED)
async def signup(user_create: UserCreate, db: Session = Depends(get_db)):
    return auth_service.signup(db, user_create)


@router.post("/login", response_model=Token)
async def login(user_login: UserLogin, db: Session = Depends(get_db)):
    return auth_service.login(db, user_login.email, user_login.password)
