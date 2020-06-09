from rest_framework import serializers
from track.serializers import TrackSerializer
from .models import Genre


class GenreSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True)

    class Meta:
        model = Genre
        fields = "__all__"
