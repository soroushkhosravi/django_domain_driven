from django.urls import path

from src.domain.add_book import add_book
from django.http import HttpResponse, JsonResponse

def add_book_view(request, book_title: str):
    add_book(book_title=book_title)
    return JsonResponse({"message": "book added successfully."})

urlpatterns = [
    path("book/<str:book_title>", add_book_view, name="add_book"),
]