from django.urls import path, include
from .auth_views import Register#, login, logout
from .views import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

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
    path('register/', Register.as_view(), name='register'),

    # JWT Authentication Endpoints
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


]

