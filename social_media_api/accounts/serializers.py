from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import CustomUser
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
User = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField()
    token = serializers.CharField(read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'bio', 'profile_picture', 'password' )
    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        token = Token.objects.create(user=user)
        user.token = token.key
        return user

from rest_framework.authtoken.models import Token
from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if user and user.is_active:
            token, created = Token.objects.get_or_create(user=user)
            data['token'] = token.key
            return data
        raise serializers.ValidationError("Invalid Credentials")