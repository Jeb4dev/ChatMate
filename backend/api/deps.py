from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from core.database import session_factory
from models.user import User
from services.users import decode_token


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/token")


def get_session() -> Session:
    return session_factory()


def get_user(token: str = Depends(oauth2_scheme), session: Session = Depends(get_session)) -> User:
    user = decode_token(session, token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


