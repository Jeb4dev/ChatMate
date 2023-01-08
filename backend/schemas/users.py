from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True


class LoginSchema(BaseModel):
    username: str
    password: str


class RegisterSchema(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
