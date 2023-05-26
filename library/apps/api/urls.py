from django.urls import path, include

from apps.api.views.authlib import ClientViewSet
from apps.api.views.book import (
    BookViewSet,
    BookUserViewSet,
    UserBookViewSet,
    BorrowedBookViewSet
)
from rest_framework import routers

#authentication Library app urls
client_router = routers.DefaultRouter()
client_router.register('' , ClientViewSet , basename= "client")
client_router.register('user_books' , UserBookViewSet , basename= "user-books")

# /user_books/ to list books related to a specific user
# /book_users/ to list users related to a specific book

#book_app_urls
book_router = routers.DefaultRouter()
book_router.register('' , BookViewSet , basename= "book")
book_router.register('borrowed', BorrowedBookViewSet , basename= "borrowed-books")
book_router.register('book_users' , BookUserViewSet , basename= "book_users")

urlpatterns = [
    path('client', include(client_router.urls)),
    path('book', include(book_router.urls)),
]
