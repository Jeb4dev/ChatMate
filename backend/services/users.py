import jwt
from datetime import datetime
from typing import Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from models.user import User
from schemas.users import TokenResponse
from core import get_settings

settings = get_settings()


def encode_token(user: User) -> str:
    token = jwt.encode(
        {"sub": user.id, "iat": datetime.utcnow().timestamp()},
        key=settings.SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM,
    )
    return token


def decode_token(session: Session, token: str) -> Optional[User]:
    data = jwt.decode(
        token,
        key=settings.SECRET_KEY,
        algorithms=[settings.JWT_ALGORITHM],
    )
    if "sub" in data:
        user = session.query(User).filter(User.id == data["sub"]).first()
        return user


def authenticate(session: Session, login: str, password: str) -> Optional[User]:
    user = session.query(User).filter(User.username == login).first()
    if user and user.hash_password(password) == user.hashed_password:
        return user


def create_user(session: Session, username: str, password: str) -> Optional[User]:
    user = session.query(User).filter(User.username == username).first()
    if not user:
        user = User(username=username)
        session.add(user)
        session.commit()
        user.set_password(session, password)
        session.commit()
        return user


def authenticate_request(session: Session, login: str, password: str) -> TokenResponse:
    user = authenticate(session, login, password)
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials")
    return TokenResponse(access_token=encode_token(user))
