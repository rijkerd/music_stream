from rest_framework import serializers
from .models import Track
from users.models import CustomUser


class TrackSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        many=False, read_only=True, slug_field='name')
    album = serializers.SlugRelatedField(
        many=False, read_only=True, slug_field='name')
    artist = serializers.SlugRelatedField(
        many=False, read_only=True, slug_field='name')
    owner = serializers.SlugRelatedField(
        many=False, read_only=True, slug_field='username')
    genre = serializers.SlugRelatedField(
        many=False, read_only=True, slug_field='name')

    class Meta:
        model = Track
        fields = "__all__"
