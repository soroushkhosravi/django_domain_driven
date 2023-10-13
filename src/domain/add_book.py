"""."""
from src.data_models.models import Book


def add_book(book_title: str):
    """Adds a book."""
    book = Book(title=book_title)
    book.save()

    return book