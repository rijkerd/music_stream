import uuid
from django.db import models
from django.db import models
from django.utils import timezone

from users.models import CustomUser
from artist.models import Artist


class Genre(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, auto_created=True)
    genreName = models.CharField(max_length=200, unique=True, blank=False)
    genre_thumbnail = models.ImageField(upload_to='genre')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.genreName


class Album(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, auto_created=True)
    albumName = models.CharField(max_length=200, unique=True, blank=False)
    album_thumbnail = models.ImageField(upload_to='album')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.albumName


class Song(models.Model):
    audio_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, auto_created=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    artist = models.ForeignKey(
        Artist, to_field='name', on_delete=models.CASCADE)
    title = models.CharField(
        max_length=200, verbose_name="Song name", blank=False, default='Title')
    description = models.CharField(max_length=200,
                                   default="", blank=False)
    genre = models.OneToOneField(
        Genre, to_field='genreName', on_delete=models.CASCADE)
    album = models.OneToOneField(
        Album, to_field='albumName', on_delete=models.CASCADE)
    song_thumbnail = models.ImageField(upload_to='songsImages')
    song_url = models.FileField(upload_to='music')
    created_on = models.DateTimeField(
        verbose_name='Created on', auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.title
