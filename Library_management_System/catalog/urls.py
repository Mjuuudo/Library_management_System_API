
from django.urls import path, include
from . import views

urlpatterns = [

     # --- Authors ---
    path('authors/', views.AuthorListCreateView.as_view(), name='author-list'),
    path('authors/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),

    # --- Books ---
    path('books/', views.BookListCreateView.as_view(), name='book-list'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),

    # --- Borrow ---
    path('borrow/', views.BorrowListCreateView.as_view(), name='borrow-list'),
    path('borrow/<int:pk>/', views.BorrowDetailView.as_view(), name='borrow-detail'),
    path('borrow/<int:pk>/return/', views.return_book, name='return-book'),
]

