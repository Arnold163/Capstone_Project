from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)  # ISBN-13 standard
    published_date = models.DateField()
    available_copies = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
    
class LibraryUser(models.Model):
    username = models.CharField(max_length=50, unique=True)#unique username
    email = models.EmailField(unique=True) #Unique email address
    date_of_membership = models.DateField(auto_now_add=True) # auto set date on creation
    active_status = models.BooleanField(default=True) # is the user active

    def __str__(self):
        return self.username
    

class CheckoutLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='checkout_logs')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='checkout_logs')
    checkout_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"
    
