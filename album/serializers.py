from rest_framework import serializers
from track.serializers import TrackSerializer
from .models import Album


class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = "__all__"
