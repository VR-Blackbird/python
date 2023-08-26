from fastapi import FastAPI
from collections import namedtuple

app = FastAPI()


Book = namedtuple("Book", ["id", "title", "author", "description", "rating"])

BOOKS = {
    Book(1, "Computer Hands-on", "Gordon Ramsay", "Book with deep computer aspects", 4)
}


@app.get("/VR/books")
def read_all_books():
    return BOOKS
