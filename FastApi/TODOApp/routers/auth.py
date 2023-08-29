from typing import Annotated
from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field
from models import User
from starlette import status
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm
from routers import todos

router = APIRouter()

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class CreateUserRequest(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
    role: str


def authenticate_user(username: str, password: str, db: todos.db_dependency):
    user = db.query(User).filter(User.username == username).first()
    if user and bcrypt_context.verify(f"{username}:{password}", user.hashed_password):
        return True
    return False


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


@router.post("/token")
def get_access_token(
    form: Annotated[OAuth2PasswordRequestForm, Depends()], db: todos.db_dependency
):
    user = authenticate_user(form.username, form.password, db)
    if not user:
        return "Authentication Failed"
    return "Authentication success"
