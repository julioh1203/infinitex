import httpx
from django.core.paginator import Paginator
from django.shortcuts import render

from core.models import Book


def home(request):
    """Return the home page"""
    return render(request, "core/home.html")


def book_items(request):
    """Return the books items used by HTMX"""
    books = Book.objects.all().order_by("-published")

    page_number = request.GET.get("page", 1)
    paginator = Paginator(books, 10)
    page_obj = paginator.get_page(page_number)

    return render(request, "core/book_items.html", {"page_obj": page_obj})
