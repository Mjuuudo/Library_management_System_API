from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model) :
    name = models.CharField( max_length = 200 )
    bio = models.CharField( max_length = 200 )

    def __str__( self ) :
        return f"Author name : {self.name}"
    
class Book(models.Model) :
    book_name = models.CharField( max_length = 200 )
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13, unique=True)
    published_date = models.DateField(blank=True, null=True)
    available = models.BooleanField(default=True)

    def __str__ ( self ) :
        return f"{self.book_name} Written By {self.author.name}"
    
class Borrow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="borrows")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="borrows")
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(blank=True, null=True)
    is_returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} borrowed {self.book.title}"

    class Meta:
        ordering = ['-borrow_date']
