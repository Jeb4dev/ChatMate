from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from models.user import User
from schemas.users import LoginSchema, UserSchema, TokenResponse, RegisterSchema
from services.users import authenticate_request, create_user, encode_token
from api.deps import get_session, get_user

router = APIRouter()


@router.get("/me", response_model=UserSchema)
async def get_current_user(user: User = Depends(get_user)):
    print(user)
    return UserSchema.from_orm(user)


@router.post("/token", response_model=TokenResponse)
async def get_token(form_data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_session)):
    return authenticate_request(session, form_data.username, form_data.password)


@router.post("/login", response_model=TokenResponse)
async def authenticate(body: LoginSchema, session: Session = Depends(get_session)):
    return authenticate_request(session, body.username, body.password)


@router.post("/register", response_model=TokenResponse)
async def register(body: RegisterSchema, session: Session = Depends(get_session)):
    user = create_user(session, body.username, body.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="This user already exists")
    return TokenResponse(access_token=encode_token(user))
