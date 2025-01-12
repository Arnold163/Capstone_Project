from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils import timezone
from .models import Book, User, CheckoutLog
from .serializers import BookSerializer, UserSerializer, CheckOutBookSerializer, ReturnBookSerializer
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated


class BookViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CheckOutLogViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['post'])
    def check_out(self, request):
        serializer = CheckOutBookSerializer(data=request.data)
        if serializer.is_valid():
            user = get_object_or_404(User, id=serializer.validated_data['user_id'])
            book = get_object_or_404(Book, id=serializer.validated_data['book_id'])

            if book.available_copies < 1:
                return Response({'error': 'No available copies'}, status=status.HTTP_400_BAD_REQUEST)

            # Perform check-out
            book.available_copies -= 1
            book.save()
            CheckoutLog.objects.create(user=user, book=book)

            return Response({'message': 'Book checked out successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def return_book(self, request):
        serializer = ReturnBookSerializer(data=request.data)
        if serializer.is_valid():
            log = CheckoutLog.objects.filter(
                user_id=serializer.validated_data['user_id'],
                book_id=serializer.validated_data['book_id'],
                return_date__isnull=True,
            ).first()

            if not log:
                return Response({'error': 'No active check-out record'}, status=status.HTTP_404_NOT_FOUND)

            # Perform return
            log.return_date = timezone.now()
            log.save()
            book = log.book
            book.available_copies += 1
            book.save()

            return Response({'message': 'Book returned successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #chekviiew
class ReturnBookView(APIView):
    def post(self, request):
        
        serializer = ReturnBookSerializer(data=request.data)
        if serializer.is_valid():
            user_id = serializer.validated_data['user_id']
            book_id = serializer.validated_data['book_id']

            # Update log and increase available copies
            log = CheckoutLog.objects.get(user_id=user_id, book_id=book_id, return_date__isnull=True)
            log.return_date = timezone.now()
            log.save()
            book = log.book
            book.available_copies += 1
            book.save()
            return Response({"message": "Book returned successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class AvailableBooksView(ListAPIView):
    """
    View for listing all books with optional filtering.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['available_copies']  # For filtering by availability
    search_fields = ['title', 'author', 'isbn']  # For search by title, author, or ISBN

    def get_queryset(self):
        # Filter books to only show those with available copies
        queryset = super().get_queryset()
        available_only = self.request.query_params.get('available', None)
        if available_only == 'true':
            queryset = queryset.filter(available_copies__gt=0)
        return queryset