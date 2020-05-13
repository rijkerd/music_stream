from rest_framework import serializers
from src.music.models import Song, Album, Genre
from src.users.models import CustomUser
from src.artist.serializers import ArtistSerializers


class GenreSerializer(serializers.ModelSerializer):
    pass


class SongSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='CustomUser.email')
    album_name = serializers.HyperlinkedIdentityField(
        view_name='album-detail', format='json')

    class Meta:
        model = Song
        fields = ['user', 'title',
                  'song_url', 'song_thumbnail', 'album_name', 'created_on']


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    songs = SongSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ['id', 'album_name', 'album_thumbnail', 'songs', 'created_on']
