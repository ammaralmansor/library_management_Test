from rest_framework.viewsets import ModelViewSet
from apps.api.serializers.authlib import ClientSerializer , RegisterClientSerializer
from apps.authlib.models import Client

class ClientViewSet (ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    

class RegisterClientViewSet (ModelViewSet):
    permission_classes =[]
    queryset = Client.objects.all()
    serializer_class = RegisterClientSerializer