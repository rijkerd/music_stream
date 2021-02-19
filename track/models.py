import uuid
from django.db import models
from users.models import User
from artist.models import Artist
from genre.models import Genre
from album.models import Album
from core.storage_backends import PublicMediaStorage


class Track(models.Model):
    pass
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(
        User, related_name='tracks', on_delete=models.CASCADE)
    artist = models.ForeignKey(
        Artist, related_name='tracks', on_delete=models.CASCADE)
    title = models.CharField(
        max_length=200, blank=False, default='Title')
    description = models.CharField(max_length=200,
                                   default="", blank=False)
    genre = models.ForeignKey(
        Genre, related_name='tracks', on_delete=models.PROTECT)
    album = models.ForeignKey(
        Album, related_name='tracks', on_delete=models.CASCADE)
    thumbnail = models.FileField(storage=PublicMediaStorage(), blank=False)
    url = models.FileField(storage=PublicMediaStorage(), blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['album', 'created_at']
        ordering = ['created_at']

    def __str__(self):
        return self.title
