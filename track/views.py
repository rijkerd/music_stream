from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Track
from .serializers import TrackSerializer


class TrackViewSet(ModelViewSet):
    lookup_field = "id"
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
