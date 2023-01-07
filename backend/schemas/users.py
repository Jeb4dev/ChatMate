from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    username: int

    class Config:
        orm_mode = True


class LoginSchema(BaseModel):
    username: str
    password: str


class RegisterSchema(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    token: str
