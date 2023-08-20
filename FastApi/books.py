from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {"title": "Title One", "author": "Author One", "category": "science"},
    {"title": "Title Two", "author": "Author Two", "category": "science"},
    {"title": "Title Three", "author": "Author Three", "category": "history"},
    {"title": "Title Four", "author": "Author Four", "category": "math"},
    {"title": "Title Five", "author": "Author Five", "category": "math"},
    {"title": "Title Six", "author": "Author Two", "category": "math"},
]


@app.get("/vr/books")
def get_all_books():
    return BOOKS


@app.get("/vr/books/title/{title}")
def get_book(title):
    for book in BOOKS:
        if book.get("title").casefold() == title.casefold():
            return book


@app.get("/vr/books/author/{author}")
def get_book(author):
    books = []
    for book in BOOKS:
        if book.get("author", "").casefold() == author.casefold():
            return book


@app.get("/vr/books/")
def get_book_by_category(category):
    books = []
    for book in BOOKS:
        if book.get("category", "").casefold() == category.casefold():
            books.append(book)
    return books
