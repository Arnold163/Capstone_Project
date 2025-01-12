from rest_framework.routers import DefaultRouter
from .views import BookViewSet, UserViewSet, CheckOutLogViewSet, AvailableBooksView
from django.urls import path, include

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book') #register the bookviewset
router.register(r'users', UserViewSet, basename='user') #register the userviewset

checkout_log = CheckOutLogViewSet.as_view({
    'post': 'check_out'
})

return_log = CheckOutLogViewSet.as_view({
    'post': 'return_book'
})

urlpatterns = [
    path('', include(router.urls)),
    path('check-out/', checkout_log, name='check_out'),
    path('return-book/', return_log, name='return_book'),
    path('books/available/', AvailableBooksView.as_view(), name='available-books'),
    
]
