from rest_framework import serializers
from music.models import Song, Album, Genre
from users.models import CustomUser
from artist.serializers import ArtistSerializers


class GenreSerializer(serializers.ModelSerializer):
    pass


class SongSerializer(serializers.ModelSerializer):
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
        model = Song
        fields = "__all__"


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    songs = SongSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = "__all__"
