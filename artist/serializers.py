from rest_framework import serializers
from .models import Artist
from track.serializers import TrackSerializer


class ArtistSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = '__all__'
