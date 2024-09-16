import httpx
from django.core.management import BaseCommand

from core.models import Book


class Command(BaseCommand):
    help = "Import books from a API"

    def handle(self, *args, **options):
        url = "https://fakerapi.it/api/v2/books?_quantity=200?_locale=pt_BR"
        response = httpx.get(url)
        if response.status_code != 200:
            self.stdout.write(self.style.ERROR("Error to get books from API"))
            return

        books = response.json()["data"]
        books_obj = []
        for book in books:
            if not Book.objects.filter(title=book["title"]).exists():
                books_obj.append(
                    Book(
                        title=book["title"],
                        author=book["author"],
                        genre=book["genre"],
                        isbn=book["isbn"],
                        description=book["description"],
                        published=book["published"],
                    )
                )

        Book.objects.bulk_create(books_obj)
