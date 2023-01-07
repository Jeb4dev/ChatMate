import jwt
from datetime import datetime
from typing import Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from models.user import User
from schemas.users import TokenResponse


def encode_token(user: User) -> str:
    token = jwt.encode({
        "sub": user.id,
        "iat": datetime.utcnow().timestamp()
    })
    return token


def decode_token(session: Session, token: str) -> Optional[User]:
    data = jwt.decode(token)
    if "sub" in data:
        user = session.query(User).filter(User.id == data["sub"]).first()
        return user


def authenticate(session: Session, login: str, password: str) -> Optional[User]:
    user = session.query(User).filter(User.username == login).first()
    if user and user.hash_password(password) == user.hashed_password:
        return user


def authenticate_request(session: Session, login: str, password: str) -> TokenResponse:
    user = authenticate(session, login, password)
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials")
    return TokenResponse(token=encode_token(user))
