from typing import Annotated, Optional
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException, Path
from pydantic import BaseModel, Field
from starlette import status
from models import Base, Todos
from database import engine, session_local

app = FastAPI()
Base.metadata.create_all(bind=engine)


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


class TodoRequest(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=5, max_length=200)
    priority: int = Field(gt=0, lt=6)
    complete: Optional[bool] = None


@app.get("/VR/todos")
def read_all_todos(db: db_dependency):
    return db.query(Todos).all()


@app.get("/VR/todos/{todo_id}", status_code=status.HTTP_200_OK)
def read_by_id(db: db_dependency, todo_id: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model:
        return todo_model
    raise HTTPException(404, "Todo not found")


@app.post("/VR/todos/create_todo", status_code=status.HTTP_201_CREATED)
def create_todo(db: db_dependency, todo_request: TodoRequest):
    check_existing = db.query(Todos).filter(Todos.title == todo_request.title).first()
    if check_existing:
        raise HTTPException(409, "Todo already exists")
    todo_model = Todos(**todo_request.model_dump())
    db.add(todo_model)
    db.commit()
