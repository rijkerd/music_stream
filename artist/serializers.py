from track.serializers import TrackSerializer
from rest_framework import serializers
from artist.models import Artist


class ArtistSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = '__all__'
