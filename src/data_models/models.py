from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        """Meta class for the model."""
        db_table = "book"
        constraints = [
            models.UniqueConstraint(
                fields=["title"], name="unique_title_book"
            )
        ]

class Publisher(models.Model):
    class Meta:
        """Meta class for the model."""
        db_table = "publisher"
    name = models.CharField(max_length=300)

    def add_book_with_tile(self, **kwargs):
        """Adds a book for a publisher."""
        book_sale = BookSale(publisher=self, **kwargs)
        book_sale.save()

class BookSale(models.Model):
    class Meta:
        """Meta class for the model."""
        db_table = "booksale"
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    pubdate = models.DateField()