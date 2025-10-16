from django.shortcuts import render
from .models import User, Author, Book, Borrowing
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import UserSerializer, AuthorSerializer, BookSerializer, BorrowingSerializer
from rest_framework import permissions


# Create your views here.

class UserListCreateView(ListCreateAPIView) :
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView) :
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class AuthorListCreateView(ListCreateAPIView) :
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.AllowAny]


class AuthorRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView) :
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.AllowAny]


class BookListCreateView(ListCreateAPIView) :
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView) :
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class BorrowingListCreateView(ListCreateAPIView) :
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer

class BorrowingRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView) :
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer

