from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Album
from .serializers import AlbumSerializer


class AlbumList(ListAPIView):
    """
    Return a list of all albums
    """
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class AlbumDetail(RetrieveAPIView):
    """
    Return an album based on an id
    """
    lookup_field = "id"
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
