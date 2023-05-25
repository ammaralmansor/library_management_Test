from django.db import models
from apps.authlib.models import Client
class Book(models.Model):
    title = models.CharField(max_length=100)
    auther = models.CharField(max_length=100)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    borrowing_price = models.DecimalField(
        max_digits=10 , 
        decimal_places=2
    )
    
    quantity = models.PositiveBigIntegerField()

    def __str__ (self):
        return self.title
    
class BorrowedBook (models.Model):
    client = models.ForeignKey(
        Client,
        on_delete= models.CASCADE,
        related_name= "borrowedbook_set"
    )
