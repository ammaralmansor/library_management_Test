from django.db import models
from django.contrib.auth.models import AbstractUser

from django.conf import settings

# class Client (AbstractUser):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     books_borrowed = models.ManyToManyField(Book , blank = True)


class Client (models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL ,
        default=1,
        on_delete=models.CASCADE,
        related_name='client_user'
    )

    def __str__(self):
        return self.user.username