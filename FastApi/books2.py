from fastapi import FastAPI, Body
from pydantic import BaseModel
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
    id: int
    title: str
    author: str
    description: str
    rating: int


@app.get("/VR/books")
def read_all_books():
    return BOOKS


@app.post("/VR/books/create_book")
def add_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(new_book._asdict())
