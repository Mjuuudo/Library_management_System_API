from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser) :
    email = models.EmailField(unique= True)
    Is_Borrowing = models.BooleanField(default=True)

    def __str__ (self) :
        return f"Username : {self.username} with email : {self.email}"

class Author(models.Model) :
    full_name = models.CharField(max_length = 100)
    Birth_Year = models.DateField(null = True)

    def __str__ (self) :
        return f"Author Name : {self.full_name}"

class Book(models.Model) :
    Book_title = models.CharField(max_length = 200)
    Author = models.ForeignKey(Author, on_delete=models.CASCADE)
    posted_Date = models.DateField()
    Number_of_Copies = models.PositiveIntegerField()
    Is_Alvalible = models.BooleanField()

    def __str__ (self) :
        return f"Book {self.Book_title} Written By {self.Author.full_name}"


class Borrowing(models.Model) :
    Book = models.ForeignKey(Book, on_delete=models.CASCADE)
    Client = models.ForeignKey(User, on_delete=models.CASCADE)
    Borrow_Date = models.DateTimeField( auto_now_add=True )
    Return_Date = models.DateTimeField()
    Returned = models.BooleanField(default=False)

    def __str__ (self) :
        return f"The Book {self.Book.Book_title} Borrowed By {self.Client.username}"



