from rest_framework import serializers
from src.users import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('id', 'username', 'email', 'date_joined')
