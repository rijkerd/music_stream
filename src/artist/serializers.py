from rest_framework import serializers
from src.artist.models import Artist


class ArtistSerializers(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'
