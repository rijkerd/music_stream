from rest_framework import serializers
from users import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('id', 'username', 'email', 'date_joined', 'last_login')
