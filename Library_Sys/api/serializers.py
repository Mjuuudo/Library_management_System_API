from rest_framework import serializers
from .models import User, Author, Book, Borrowing

class UserSerializer(serializers.ModelSerializer) :
    class Meta :
        model = User
        fields = ['id', 'username', 'email', 'Is_Borrowing']

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