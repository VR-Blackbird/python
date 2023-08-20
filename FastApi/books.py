from fastapi import FastAPI, Body

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
    for book in BOOKS:
        if book.get("author", "").casefold() == author.casefold():
            yield book


@app.get("/vr/books/")
def get_book_by_category(category):
    for book in BOOKS:
        if book.get("category", "").casefold() == category.casefold():
            yield book


@app.get("/vr/books/{author}")
def get_book_by_author_category(author: str, category: str):
    for book in BOOKS:
        if (
            book.get("author").casefold() == author.casefold()
            and book.get("category").casefold() == category.casefold()
        ):
            yield book


@app.post("/vr/books/create_book")
def add_book(book=Body()):
    BOOKS.append(book)


@app.put("/vr/books/update_book")
def update_book(my_book=Body()):
    for book in BOOKS:
        if book.get("title").casefold() == my_book.get("title").casefold():
            book.update(my_book)


@app.delete("/vr/books/delete_book")
def delete_book(title):
    for index, book in enumerate(BOOKS):
        if book.get("title").casefold() == title.casefold():
            BOOKS.pop(index)
            break
