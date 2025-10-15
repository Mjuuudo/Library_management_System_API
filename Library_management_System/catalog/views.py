from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.utils import timezone
from .models import Author, Book, Borrow
from .serializers import AuthorSerializer, BookSerializer, BorrowSerializer


# Create your views here.
class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.AllowAny]


class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.AllowAny]



class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class BorrowListCreateView(generics.ListCreateAPIView):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        book = serializer.validated_data['book']
        if not book.available:
            raise ValueError("This book is not available.")
        book.available = False
        book.save()
        serializer.save(user=self.request.user)


class BorrowDetailView(generics.RetrieveAPIView):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer
    permission_classes = [permissions.AllowAny]


@api_view(['PUT'])
def return_book(request, pk):
    try:
        borrow = Borrow.objects.get(pk=pk)
    except Borrow.DoesNotExist:
        return Response({"detail": "Borrow record not found."}, status=status.HTTP_404_NOT_FOUND)

    if borrow.is_returned:
        return Response({"detail": "Book already returned."}, status=status.HTTP_400_BAD_REQUEST)

    borrow.is_returned = True
    borrow.return_date = timezone.now()
    borrow.book.available = True
    borrow.book.save()
    borrow.save()

    return Response({"detail": "Book returned successfully."}, status=status.HTTP_200_OK)