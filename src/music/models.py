import uuid
from django.db import models
from django.db import models
from django.utils import timezone

from users.models import CustomUser
from artist.models import Artist


class Genre(models.Model):
    genre_name = models.CharField(max_length=200, unique=True, blank=False)
    genre_thumbnail = models.ImageField(upload_to='genre')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.genre_name


class Album(models.Model):
    album_name = models.CharField(max_length=200, unique=True, blank=False)
    album_thumbnail = models.ImageField(upload_to='album')
    created_on = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     unique_together = ['album', 'order']
    #     ordering = ['created_on']

    def __str__(self):
        return self.album_name


class Song(models.Model):
    id = models.IntegerField(
        primary_key=True, auto_created=True, blank=False, unique=True,)
    user = models.ForeignKey(
        CustomUser, related_name='uploader_name', on_delete=models.CASCADE)
    artist = models.ForeignKey(
        Artist, related_name='song_creator', on_delete=models.CASCADE)
    title = models.CharField(
        max_length=200, verbose_name="Song name", blank=False, default='Title')
    description = models.CharField(max_length=200,
                                   default="", blank=False)
    genre = models.ForeignKey(
        Genre, related_name='song_genre', on_delete=models.CASCADE)
    album = models.ForeignKey(
        Album, related_name='songs', on_delete=models.CASCADE)
    song_thumbnail = models.ImageField(upload_to='songsImages')
    song_url = models.FileField(upload_to='music')
    created_on = models.DateTimeField(
        verbose_name='Created on', auto_now_add=True)

    class Meta:
        unique_together = ['album', 'created_on']
        ordering = ['created_on']

    def __str__(self):
        return self.title
