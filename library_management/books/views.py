from django.shortcuts import render
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
# Create your views here.

class BookviewSet(viewsets.ModelViewSet):
    """aviewset for managing books in the libraty"""

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    