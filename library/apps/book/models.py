from typing import Iterable, Optional
from django.db import models
from apps.authlib.models import Client


class Book(models.Model):
    title = models.CharField(max_length=100)
    auther = models.CharField(max_length=100)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    borrowing_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    quantity = models.PositiveBigIntegerField()

    def __str__(self):
        return self.title


class BorrowedBook (models.Model):
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name="borrowedbook_set"
    )
    book = models.ForeignKey(
        Book,
        default=1,
        on_delete=models.CASCADE,
        related_name='borrowing_user_set'
    )
    borrowed_date = models.DateTimeField(auto_now_add=True , null = True , blank= True)

    def __str__(self):
        return f'{self.client} borrowed {self.book}'
    
    def save(self, *args, **kwargs):
        if self.book.quantity>0 :
            self.book.quantity -=1
            if self.book.quantity == 0:
                self.book.is_active = False
            self.book.save()
            super().save(*args, **kwargs)

        else:
            raise ValueError("Book is not available")
        