from rest_framework import mixins
from rest_framework.viewsets import (
    ModelViewSet,
    GenericViewSet,
    ReadOnlyModelViewSet
)
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


class BorrowedBookViewSet (
    mixins.CreateModelMixin ,
    mixins.RetrieveModelMixin ,
    mixins.ListModelMixin ,
    mixins.DestroyModelMixin,
    GenericViewSet
            ):

    queryset = BorrowedBook.objects.all()
    serializer_class = BorrowedBookSerializer


class UserBookViewSet (ReadOnlyModelViewSet):
    queryset = Client.objects.all()
    serializer_class = UserBookSerializer


class BookUserViewSet (ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookUsersSerializer

