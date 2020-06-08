from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Artist
from .serializers import ArtistSerializer


class ArtistList(ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ArtistDetail(RetrieveAPIView):
    lookup_field = "id"
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
