from typing import Annotated, Optional
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Path, Request
from pydantic import BaseModel, Field
from starlette import status
from models import Todos
from database import session_local
from routers.auth import verify_user
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="templates")


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(verify_user)]


class TodoRequest(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=5, max_length=200)
    priority: int = Field(gt=0, lt=6)
    complete: Optional[bool] = None


@router.get("/test")
def test(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@router.get("/VR/todos", status_code=status.HTTP_200_OK)
def read_all_todos(user: user_dependency, db: db_dependency):
    return db.query(Todos).filter(Todos.owner_id == user.get("id", "")).all()


@router.get("/VR/todos/{todo_id}", status_code=status.HTTP_200_OK)
def read_by_id(user: user_dependency, db: db_dependency, todo_id: int = Path(gt=0)):
    if not user:
        raise HTTPException(404, "User not found")
    todo_model = (
        db.query(Todos)
        .filter(Todos.id == todo_id, Todos.owner_id == user.get("id", ""))
        .first()
    )
    if todo_model:
        return todo_model
    raise HTTPException(404, "Todo not found")


@router.post("/VR/todos/create_todo", status_code=status.HTTP_201_CREATED)
def create_todo(user: user_dependency, db: db_dependency, todo_request: TodoRequest):
    if not user:
        raise HTTPException(404, "User not found")
    check_existing = (
        db.query(Todos)
        .filter(
            Todos.title == todo_request.title,
            Todos.description == todo_request.description,
        )
        .first()
    )
    todo_model = Todos(**todo_request.model_dump(), owner_id=user.get("id"))
    if check_existing:
        raise HTTPException(409, "Todo already exists")

    db.add(todo_model)
    db.commit()


@router.put("/VR/todos/update_todo", status_code=status.HTTP_204_NO_CONTENT)
def update_todo(
    user: user_dependency, db: db_dependency, todo_id: int, todo_request: TodoRequest
):
    if not user:
        raise HTTPException(404, "User not found")
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if not todo_model:
        raise HTTPException(204, "Todo not found")
    table = Todos.__table__
    statement = (
        table.update().where(Todos.id == todo_id).values(**todo_request.model_dump())
    )
    db.execute(statement)
    db.commit()


@router.delete("/VR/todos/delete_todo", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(user: user_dependency, db: db_dependency, todo_id: int):
    if not user:
        raise HTTPException(404, "User not found")
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if not todo_model:
        raise HTTPException(204, "Todo not found")

    db.delete(todo_model)
    db.commit()
