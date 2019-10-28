from django.shortcuts import render
from rest_framework import viewsets

from music.models import Song
from music.serializers import SongSerializer


class MusicListView(viewsets.ReadOnlyModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
