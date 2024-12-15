from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'bio', 'profile_picture', 'password' )
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

from rest_framework.authtoken.models import Token
from rest_framework import serializers

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('key',)