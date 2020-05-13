# import uuid
from django.db import models


class Artist(models.Model):
    id = models.AutoField(
        primary_key=True, auto_created=True, blank=False, unique=True)
    name = models.CharField(max_length=200, blank=False, unique=True)
    biography = models.CharField(max_length=200, blank=False)
    photo_url = models.ImageField(upload_to='artist', blank=False)
    created_at = models.DateTimeField(
        verbose_name='Created At', auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.name
