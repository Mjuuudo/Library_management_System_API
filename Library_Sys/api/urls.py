from django.urls import path, include
from .auth_views import register, login, logout
from .views import *

urlpatterns = [
    #End points for User
    path('users/', UserListCreateView.as_view(), name='user-list-create'), 
    path('users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-detail'),
    
    #End points for Author
    path('authors/', AuthorListCreateView.as_view(), name='author-list-create'),
    path('authors/<int:pk>/', AuthorRetrieveUpdateDestroyView.as_view(), name='author-detail'),

    #End points for Book
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-detail'),

    #End points for Borrowing
    path('borrowings/', BorrowingListCreateView.as_view(), name='borrowing-list-create'),
    path('borrowings/<int:pk>/', BorrowingRetrieveUpdateDestroyView.as_view(), name='borrowing-detail'),

    # Authentication Endpoints
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),


]

