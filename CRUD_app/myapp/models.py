from django.db import models

# Create your models here.
class Book(models.Model):
    book_name =models.CharField(max_length=90)
    book_author =models.CharField(max_length=90)
    book_price =models.IntegerField()
