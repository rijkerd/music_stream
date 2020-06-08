from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Track
from .serializers import TrackSerializer


class TrackList(ListAPIView):
    """
    Return a list of all tracks
    """
    queryset = Track.objects.all()
    serializer_class = TrackSerializer


class TrackDetail(RetrieveAPIView):
    """
    Return a details of a track based on the id
    """
    lookup_field = "id"
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
