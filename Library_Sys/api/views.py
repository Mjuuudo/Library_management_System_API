from django.shortcuts import render
from .models import User, Author, Book, Borrowing
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .serializers import *
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
    
    def get_permissions(self):
        # Anyone can list books, only admin/staff can create
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]


class BookRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView) :
    queryset = Book.objects.all()
    serializer_class = BookSerializer


    def get_permissions(self):
        # Anyone can list books, only admin/staff can create
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]
    
class BookAlvalibleShowAPIView(ListAPIView):
    queryset = Book.objects.filter(Number_of_Copies__gt=0)
    serializer_class = BookAlvalibleShowSerializer
    permission_classes = [permissions.AllowAny]


class BorrowingListCreateView(ListCreateAPIView):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Borrowing.objects.filter(Client=self.request.user)

    def perform_create(self, serializer):
        serializer.save(Client=self.request.user)

class BorrowingRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView) :
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer
    permission_classes = [permissions.IsAuthenticated]

