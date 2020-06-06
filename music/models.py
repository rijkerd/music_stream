import uuid
from django.db import models

from users.models import CustomUser
from artist.models import Artist


class Genre(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, unique=True, blank=False)
    thumbnail = models.ImageField(upload_to='genre')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.name


class Album(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, unique=True, blank=False)
    thumbnail = models.ImageField(upload_to='album')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # class Meta:
    #     unique_together = ['album', 'order']
    #     ordering = ['created_on']

    def __str__(self):
        return self.name


class Song(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(
        CustomUser, related_name='uploader_name', on_delete=models.CASCADE)
    artist = models.ForeignKey(
        Artist, related_name='song_creator', on_delete=models.CASCADE)
    title = models.CharField(
        max_length=200, verbose_name="Song name", blank=False, default='Title')
    description = models.CharField(max_length=200,
                                   default="", blank=False)
    genre = models.ForeignKey(
        Genre, related_name='song_genre', on_delete=models.PROTECT)
    album = models.ForeignKey(
        Album, related_name='songs', on_delete=models.CASCADE)
    song_thumbnail = models.ImageField(upload_to='songsImages')
    song_url = models.FileField(upload_to='music')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['album', 'created_at']
        ordering = ['created_at']

    def __str__(self):
        return self.title
