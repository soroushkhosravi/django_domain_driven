"""Tests related to the publisher model."""
import pytest
from src.data_models.models import Publisher, BookSale, Book
from datetime import datetime
from django.db.models import Count, Q
from django.db.utils import IntegrityError


@pytest.mark.django_db(reset_sequences=True)
def test_getting_publishers_with_more_than_one_book():
    """Tests we can get publishers with more than on book."""
    publisher_1 = Publisher.objects.create(name="pub 1")
    publisher_2 = Publisher.objects.create(name="pub 2")
    publisher_3 = Publisher.objects.create(name="pub 3")
    publisher_4 = Publisher.objects.create(name="pub 4")

    book_1 = BookSale.objects.create(
        name="book 1",
        pages=10,
        price=100.25,
        rating=15,
        pubdate=datetime.now(),
        publisher=publisher_1
    )
    book_2 = BookSale.objects.create(
        name="book 2",
        pages=10,
        price=100.25,
        rating=15,
        pubdate=datetime.now(),
        publisher=publisher_1
    )

    pubs_with_more_or_equal_one_book = Publisher.objects.annotate(
        num_books=Count("booksale", distinct=True)
    ).filter(
        num_books__gte=1
    ).order_by('-num_books')

    assert len(pubs_with_more_or_equal_one_book) == 1
    assert isinstance(pubs_with_more_or_equal_one_book[0], Publisher)
    assert pubs_with_more_or_equal_one_book[0].id == 1
    assert pubs_with_more_or_equal_one_book[0].booksale_set.all()[0] == book_1
    assert pubs_with_more_or_equal_one_book[0].booksale_set.all()[1] == book_2

    assert pubs_with_more_or_equal_one_book[0].num_books == 2


@pytest.mark.django_db(reset_sequences=True)
def test_get_book_by_its_id_returns_expected__book():
    """."""
    book_1 = Book(title="1")
    book_2 = Book(title="2")
    book_3 = Book(title="3")
    book_1.save()
    book_2.save()
    book_3.save()

    book = Book.objects.get(id="1")

    assert book.id == 1
    assert book.title == "1"


@pytest.mark.django_db(reset_sequences=True)
def test_two_different_books_can_not_have_same_title():
    """."""
    book_1 = Book(title="1")
    book_2 = Book(title="1")
    book_1.save()

    with pytest.raises(IntegrityError) as error:
        book_2.save()

@pytest.mark.django_db(reset_sequences=True)
def test_two_different_books_can_not_have_same_title_if_created_through_manager():
    """."""
    Book.objects.create(title="1")

    with pytest.raises(IntegrityError) as error:
        Book.objects.create(title="1")

