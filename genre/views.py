from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Genre
from .serializers import GenreSerializer


class GenreViewSet(ModelViewSet):
    lookup_field = "id"
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
