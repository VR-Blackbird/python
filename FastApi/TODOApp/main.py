from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException, Path
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


@app.get("/VR/todos")
def read_all_todos(db: db_dependency):
    return db.query(Todos).all()


@app.get("/VR/todos/{todo_id}", status_code=status.HTTP_200_OK)
def read_by_id(db: db_dependency, todo_id: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model:
        return todo_model
    raise HTTPException(404, "Todo not found")
