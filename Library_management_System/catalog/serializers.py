from rest_framework import serializers
from .models import Author, Book, Borrow

# Here We Can Found Our Serializers

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(), source='author', write_only=True
    )

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'author_id', 'isbn', 'published_date', 'available']

class BorrowSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    book = BookSerializer(read_only=True)
    book_id = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.filter(available=True),
        source='book',
        write_only=True
    )

    class Meta:
        model = Borrow
        fields = ['id', 'user', 'book', 'book_id', 'borrow_date', 'return_date', 'is_returned']