from typing import Annotated
from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field
from models import User
from datetime import timedelta, datetime
from starlette import status
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt
from routers import todos


router = APIRouter()
SECRET_KEY = "8f17dcb1ab1ef7dc13194f4b75f34182a2712130ab68e762597477587fcccb0c"
ALGORITHM = "HS256"
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class CreateUserRequest(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
    role: str


class Token(BaseModel):
    access_token: str
    token_type: str


def authenticate_user(username: str, password: str, db: todos.db_dependency):
    user = db.query(User).filter(User.username == username).first()
    if user and bcrypt_context.verify(f"{username}:{password}", user.hashed_password):
        return user
    return False


def create_access_token(username: str, user_id: int, expires_delta: timedelta):
    encode = {"sub": username, "id": user_id}
    expires = datetime.utcnow() + expires_delta
    encode.update({"exp": expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


@router.post("/auth/", status_code=status.HTTP_201_CREATED)
def create_user(db: todos.db_dependency, create_user_request: CreateUserRequest):
    create_user_model = User(
        email=create_user_request.email,
        username=create_user_request.username,
        first_name=create_user_request.first_name,
        last_name=create_user_request.last_name,
        role=create_user_request.role,
        hashed_password=bcrypt_context.hash(
            f"{create_user_request.username}:{create_user_request.password}"
        ),
        is_active=True,
    )
    db.add(create_user_model)
    db.commit()


@router.post("/token", response_model=Token)
def get_access_token(
    form: Annotated[OAuth2PasswordRequestForm, Depends()], db: todos.db_dependency
):
    user = authenticate_user(form.username, form.password, db)
    if not user:
        return "Authentication Failed"
    token = create_access_token(user.username, user.id, timedelta(minutes=20))
    return {"access_token": token, "token_type": "bearer"}
