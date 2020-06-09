from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Album
from .serializers import AlbumSerializer


class AlbumViewSet(ModelViewSet):
    lookup_field = "id"
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
