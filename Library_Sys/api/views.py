from django.shortcuts import render
from .models import User, Author, Book, Borrowing
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import UserSerializer, AuthorSerializer, BookSerializer, BorrowingSerializer


# Create your views here.

class UserListCreateView(ListCreateAPIView) :
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView) :
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AuthorListCreateView(ListCreateAPIView) :
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView) :
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookListCreateView(ListCreateAPIView) :
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView) :
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BorrowingListCreateView(ListCreateAPIView) :
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer

class BorrowingRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView) :
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer

