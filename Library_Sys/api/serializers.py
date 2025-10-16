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

class BookSerializer(serializers.ModelSerializer) :
    Author = AuthorSerializer(read_only=True)
    
    class Meta :
        model = Book
        fields = ['id', 'Book_title', 'Author', 'posted_Date', 'Number_of_Copies', 'Is_Alvalible']

class BorrowingSerializer(serializers.ModelSerializer) :
    Book = BookSerializer(read_only=True)
    Client = UserSerializer(read_only=True)
    
    class Meta :
        model = Borrowing
        fields = ['id', 'Book', 'Client', 'Borrow_Date', 'Return_Date', 'Returned']

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user if request else None
        borrowing = Borrowing.objects.create(Client=user, **validated_data)
        return borrowing

    def validate(self, data):
        book = data.get('Book')
        if book and not book.Is_Alvalible:
                raise serializers.ValidationError("This book is currently not available for borrowing.")
        return data