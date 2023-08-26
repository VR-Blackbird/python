from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field
from collections import namedtuple

app = FastAPI()


Book = namedtuple("Book", ["id", "title", "author", "description", "rating"])


BOOKS = [
    Book(
        1, "Computer Hands-on", "Gordon Ramsay", "Book with deep computer aspects", 4
    )._asdict(),
    Book(
        2, "Data structures and Algorithms deep dive", "Venkat", "Advanced concepts", 3
    )._asdict(),
    Book(3, "Graph theory", "Gamilia", "Dupe", 5)._asdict(),
]


class BookRequest(BaseModel):
    id: Optional[int]
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(ge=0, le=5)


@app.get("/VR/books")
def read_all_books():
    return BOOKS


@app.post("/VR/books/create_book")
def add_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(add_book_id(new_book._asdict()))


def add_book_id(book):
    book["id"] = 1 if len(BOOKS) == 0 else BOOKS[-1]["id"] + 1
    return book
