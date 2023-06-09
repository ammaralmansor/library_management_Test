from django.urls import path, include
from apps.api.views.authlib import (
    ClientViewset,
    RegisterClientView,
)
from apps.api.views.book import (
    BookViewSet,
    BookUsersViewSet,
    UserBooksViewSet,
    BorrowedBookViewSet,
)
from rest_framework import routers
from rest_framework.authtoken.views import ObtainAuthToken

# authlibrary app urls
client_router = routers.DefaultRouter()
client_router.register('', ClientViewset, basename='client')
client_router.register('user_books', UserBooksViewSet, basename='user-books')

# /user_books/ to list books related to a specific user
# /book_users/ to list users related to a specific book

# book app urls
book_router = routers.DefaultRouter()
book_router.register('', BookViewSet, basename='book')
book_router.register('book_users', BookUsersViewSet, basename='book-users')

router = routers.DefaultRouter()
router.register('', BorrowedBookViewSet, basename='borrowing-books')


urlpatterns = [
    path('register/', RegisterClientView.as_view(), name='register'),
    path('login/', ObtainAuthToken.as_view(), name='api_token_auth'),

    path('client/', include(client_router.urls)),
 
    path('book/', include(book_router.urls)),
    path('borrowing/', include(router.urls)),
]
