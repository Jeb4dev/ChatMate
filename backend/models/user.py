import base64

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from core.database import Base
from hashlib import sha512
from secrets import token_bytes


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    salt = Column(String, default=lambda: base64.b64encode(token_bytes(16)).decode())
    hashed_password = Column(String)

    def hash_password(self, password: str) -> str:
        return sha512((password + self.salt).encode("utf-8")).hexdigest()

    def set_password(self, session: Session, password: str):
        self.hashed_password = self.hash_password(password)
        session.commit()
