from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        """Meta class for the model."""
        db_table = "book"

class Publisher(models.Model):
    class Meta:
        """Meta class for the model."""
        db_table = "publisher"
    name = models.CharField(max_length=300)

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