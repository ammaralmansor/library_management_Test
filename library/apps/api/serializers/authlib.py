from rest_framework import serializers
from apps.authlib.models import Client
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username', 'email'
        )


class ClientSerializer (serializers.ModelSerializer):
    details = UserSerializer(
        read_only=True,
        source='user_id'
    )

    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        write_only=True

    )

    class Meta:
        model = Client
        fields = [
            'id',
            'user_id',
            # ExtraField
            'details'
        ]


class RegisterClientSerializer(serializers.ModelSerializer):
    """
    for registering a new client user
    """
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Client
        fields = ('username', 'password')

    def create(self, validate_data):
        password = validate_data.pop['password']
        user_data = {
            'username': validate_data['username'],
            'password': password
        }

        user = User.objects.create_user(**user_data)
        user.set_password(password)
        user.save()

        ModelClass = self.Meta.model
        Client_obj = ModelClass._default_manager.create(
            user=user
        )
        return Client_obj
