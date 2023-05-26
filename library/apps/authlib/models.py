from django.db import models
from django.contrib.auth.models import User


# class Client (AbstractUser):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     books_borrowed = models.ManyToManyField(Book , blank = True)


class Client (models.Model):
    user_id = models.OneToOneField(
        User ,
        default=1,
        on_delete=models.CASCADE,
        related_name='client_user'
    )

    def __str__(self):
        return self.user_id.username