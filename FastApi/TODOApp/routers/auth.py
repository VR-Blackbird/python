from fastapi import APIRouter
from pydantic import BaseModel, Field
from models import User
from starlette import status
from passlib.context import CryptContext
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
