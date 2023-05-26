from django.urls import path, include

from apps.api.views.authlib import (
    ClientViewSet,
    RegisterClientViewSet
)


from apps.api.views.book import (
    BookViewSet,
    BookUserViewSet,
    UserBookViewSet,
    BorrowedBookViewSet
)
from rest_framework import routers
from rest_framework.authtoken.views import ObtainAuthToken

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

router = routers.DefaultRouter()
router.register('borrowing' , BorrowedBookViewSet , basename="borrowing-books")

urlpatterns = [
    path('register/' , RegisterClientViewSet.as_view() , name = "register"),
    path('login/' , ObtainAuthToken.as_view(), name="api_token_auth"),
    path('client/', include(client_router.urls)),
    path('borrowing/', include(router.urls)),
    path('book/', include(book_router.urls)),
]
