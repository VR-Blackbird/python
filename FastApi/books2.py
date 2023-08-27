from typing import Optional

from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from starlette import status
from collections import namedtuple

app = FastAPI()


Book = namedtuple(
    "Book", ["id", "title", "author", "description", "rating", "published_date"]
)


class BookRequest(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(ge=0, le=5)
    published_date: int

    class Config:
        json_schema_extra = {
            "example": {
                "title": "A new book",
                "author": "Bombarded",
                "description": "Something got bombarded",
                "rating": 4,
                "published_date": 1987,
            }
        }


BOOKS = [
    Book(
        1,
        "Computer Hands-on",
        "Gordon Ramsay",
        "Book with deep computer aspects",
        4,
        2012,
    )._asdict(),
    Book(
        2,
        "Data structures and Algorithms deep dive",
        "Venkat",
        "Advanced concepts",
        5,
        2011,
    )._asdict(),
    Book(3, "Graph theory", "Gamilia", "Dupe", 5, 2011)._asdict(),
]


@app.get("/VR/books", status_code=status.HTTP_200_OK)
def read_all_books():
    return BOOKS


@app.get("/VR/books/{book_id}", status_code=status.HTTP_200_OK)
def get_book_by_id(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book["id"] == book_id:
            return book
    raise HTTPException(404, "Book not found")


@app.get("/VR/books/rating/", status_code=status.HTTP_200_OK)
def get_book_by_rating(rating: int = Query(ge=0, le=5)):
    for book in BOOKS:
        if book["rating"] == rating:
            yield book


@app.get("/VR/books/publish/", status_code=status.HTTP_200_OK)
def get_book_by_date(published_date: int = Query(gt=1000)):
    for book in BOOKS:
        if book["published_date"] == published_date:
            yield book


@app.put("/VR/books/update_book", status_code=status.HTTP_204_NO_CONTENT)
def update_book(book_request: BookRequest):
    for book in BOOKS:
        if book["id"] == book_request.id:
            book.update(book_request)


@app.delete("/VR/books/delete_book/", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int = Query(gt=0)):
    book_popped = None
    for index, book in enumerate(BOOKS):
        if book["id"] == book_id:
            book_popped = BOOKS.pop(index)
            break
    if not book_popped:
        raise HTTPException(404, "Item not found")


@app.post("/VR/books/create_book", status_code=status.HTTP_201_CREATED)
def add_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(add_book_id(new_book._asdict()))


def add_book_id(book):
    book["id"] = 1 if len(BOOKS) == 0 else BOOKS[-1]["id"] + 1
    return book
