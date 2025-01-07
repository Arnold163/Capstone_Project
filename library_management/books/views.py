from django.shortcuts import render
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset for managing books in the library.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
