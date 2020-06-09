from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Artist
from .serializers import ArtistSerializer


class ArtistViewSet(ModelViewSet):
    lookup_field = "id"
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
