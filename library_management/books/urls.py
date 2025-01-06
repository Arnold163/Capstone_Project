from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from django.urls import path
from . import views

#router = DefaultRouter()
#router.register(r'books', BookViewSet, basename='book')

#urlpatterns = router.urls
urlpatterns = [
    path('books/', views.BookListView.as_view(), name='book-list'),  # Update this if using ViewSets
]