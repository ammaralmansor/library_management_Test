from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView
from apps.api.serializers.authlib import (
    ClientSerializer,
    RegisterClientSerializer,
)
from apps.authlib.models import Client


class ClientViewset(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class RegisterClientView(CreateAPIView):
    """
    View to register a new user.
    Permissions: None
    """
    permission_classes = []
    queryset = Client.objects.all()
    serializer_class = RegisterClientSerializer
