from rest_framework import serializers
from .models import User, Author, Book, Borrowing

class UserSerializer(serializers.ModelSerializer) :
    class Meta :
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data) :
        user = User.objects.create_user(**validated_data)
        return user

class AuthorSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Author
        fields = ['id', 'full_name', 'Birth_Year']

class BookSerializer(serializers.ModelSerializer):
    Author = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all()
    )

    class Meta:
        model = Book
        fields = ['id', 'Book_title', 'Author', 'posted_Date', 'Number_of_Copies', 'Is_Alvalible']

class BorrowingSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    Client = UserSerializer(read_only=True)
    # Books = Book.objects.all()
    Book_id = serializers.PrimaryKeyRelatedField(
        queryset = Book.objects.all(),
        source='Book',          # tells DRF this field actually sets the 'Book' model field
        write_only=True
    )

    class Meta:
        model = Borrowing
        fields = ['id', 'book', 'Book_id', 'Client', 'Borrow_Date', 'Return_Date', 'Returned']

    def validate(self, data):
        book = data.get('book')
        if book and not book.Is_Alvalible:
            raise serializers.ValidationError("This book is currently not available for borrowing.")
        return data
    