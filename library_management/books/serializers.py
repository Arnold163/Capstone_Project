from rest_framework import serializers
from .models import Book, User, CheckoutLog


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_isbn(self, value):
        if len(value) != 13:
            raise serializers.ValidationError("ISBN must be 13 characters long.")
        return value
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CheckoutLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckoutLog
        fields = '__all__'

class ReturnBookSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    book_id = serializers.IntegerField()


class CheckOutBookSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    book_id = serializers.IntegerField()

    def validate(self, data):
        user_id = data['user_id']
        book_id = data['book_id']

        # Check if the book exists and has available copies
        try:
            book = Book.objects.get(id=book_id)
            if book.available_copies < 1:
                raise serializers.ValidationError("No copies of the book are available.")
        except Book.DoesNotExist:
            raise serializers.ValidationError("The book does not exist.")

        # Ensure the user doesn't already have this book checked out
        if CheckoutLog.objects.filter(user_id=user_id, book_id=book_id, return_date__isnull=True).exists():
            raise serializers.ValidationError("The user already has this book checked out.")

        return data
