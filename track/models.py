import uuid
from django.db import models
from users.models import CustomUser
from artist.models import Artist
from genre.models import Genre
from album.models import Album


class Track(models.Model):
    pass
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(
        CustomUser, related_name='tracks', on_delete=models.CASCADE)
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
    thumbnail = models.ImageField(upload_to='tracks/images')
    url = models.FileField(upload_to='music')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['album', 'created_at']
        ordering = ['created_at']

    def __str__(self):
        return self.title
