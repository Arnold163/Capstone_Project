from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)  # ISBN-13 standard
    published_date = models.DateField()
    copies_available = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title