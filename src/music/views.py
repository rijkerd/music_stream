from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from .models import Song, Album
from .serializers import SongSerializer, AlbumSerializer


class SongList(ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class SongDetail(RetrieveUpdateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class AlbumList(ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class AlbumDetails(RetrieveUpdateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

# class GenreDetails

# class MusicListView(viewsets.ReadOnlyModelViewSet):
#     queryset = Song.objects.all()
#     serializer_class = SongSerializer


# class AlbumListView(viewsets.ReadOnlyModelViewSet):
#     queryset = Album.objects.all()
#     serializer_class = AlbumSerializer
