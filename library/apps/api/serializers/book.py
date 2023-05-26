from rest_framework import serializers
from apps.book.models import Book,BorrowedBook
from apps.authlib.models import Client
from apps.api.serializers.authlib import ClientSerializer
from datetime import datetime

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

        def validate(self,attrs):
            if self.context['request'] == 'POST':
                active = attrs.get('is_active', None)
                if not active:
                    raise serializers.ValidationError(
                        "Book is not avaliable"
                    )
            return super().validate(attrs)

class BorrowedBookSerializer (serializers.ModelSerializer):
    class Meta:
        model = BorrowedBook
        fields = [
            'client_id',
            'book_id',
            'borrowed_date'
        ]

    def create (self,validate_data):
        return super().create(validate_data)
    


class UserBookSerializer (serializers.ModelSerializer):
    
    books = BorrowedBookSerializer(
        many=True,
        read_only=True,
        source = 'borrowedbook_set'
    )

    user_details = ClientSerializer(
        source = 'user_id',
        read_only=True
    )
    class Meta:
        model = Client
        fields =['user_id' , 'books', 'user_details']

    def get_user_details(self,obj):
        return ClientSerializer(obj).data


class BookUsersSerializer (serializers.ModelSerializer):
    users = ClientSerializer(
        many=True,
        read_only=True,
        source = "borrowing_user_set.user.username"
    )

    book_details = BookSerializer(
        source = 'id',
        read_only = True
    )
    class Meta:
        model = Book
        fields = ["id","users","book_details"]

    def get_book_details(self,obj):
        return BookSerializer(obj).data