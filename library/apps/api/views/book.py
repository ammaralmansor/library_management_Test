from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from apps.api.serializers.book import BookSerializer
from apps.book.models import Book
from apps.book.models import BorrowedBook
from apps.api.serializers.book import (
    UserBookSerializer,
    BookUsersSerializer,
    BorrowedBookSerializer
)
from apps.authlib.models import Client

class BookViewSet (ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BorrowedBookViewSet (ModelViewSet):
    queryset = BorrowedBook.objects.all()
    serializer_class = BorrowedBookSerializer


class UserBookViewSet (ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = UserBookSerializer


class BookUserViewSet (ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookUsersSerializer

