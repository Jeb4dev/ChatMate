from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from core.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    @staticmethod
    def hash_password(password: str) -> str:
        pass

    def set_password(self, session: Session, password: str):
        pass
