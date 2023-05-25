from rest_framework import serializers
from apps.book.models import Book,BorrowedBook
from apps.authlib.models import Client
from apps.api.serializers.authlib import ClientSerializer

class BookSerializer (serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'auther',
            'description',
            'is_active',
            'borrowing_price',
            'quantity'
        ]


class BorrowedBookSerializer (serializers.ModelSerializer):
    class Meta:
        model = BorrowedBook
        fields = [
            'client',
            'book',
            'borrowed_date'
        ]


class UserBookSerializer (serializers.ModelSerializer):
    
    books = BorrowedBookSerializer(
        many=True,
        read_only=True,
        source = 'borrowedbook_set'
    )

    class Meta:
        model = Client
        fields =['user' , 'books']


class BookUsersSerializer (serializers.ModelSerializer):
    users = ClientSerializer(
        many=True,
        read_only=True,
        source = "borrowing_user_set.user.username"
    )

    class Meta:
        model = Book
        fields = ["title" , "auther" , "users"]