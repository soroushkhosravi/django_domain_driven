""""""
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import path

from src.domain.add_book import add_book


def add_book_view(request, book_title: str):
    add_book(book_title=book_title)
    return JsonResponse({"message": "book added successfully."})


def index(request):
    """The index function to render an html file."""
    return render(request, "index.html", {"foo": "bar"})

urlpatterns = [
    path("book/<str:book_title>", add_book_view, name="add_book"),
    path("index", index, name="index"),
]