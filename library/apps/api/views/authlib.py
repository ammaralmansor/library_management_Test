from rest_framework.viewsets import ModelViewSet
from apps.api.serializers.authlib import ClientSerializer
from apps.authlib.models import Client

class ClientViewSet (ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer