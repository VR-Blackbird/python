from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends
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


@app.get("/VR/books")
def read_books(db: db_dependency):
    return db.query(Todos).all()
