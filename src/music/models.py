import uuid
from django.db import models
from django.db import models
from django.utils import timezone

from users.models import CustomUser


class Song(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    audio_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, auto_created=True)
    title = models.CharField(
        max_length=200, verbose_name="Song name", blank=False, default='Title')
    description = models.TextField(
        default="This is the description", blank=False)
    created_at = models.DateTimeField(
        verbose_name='Created At', auto_now_add=True)
    thumbnail = models.ImageField(upload_to='thumbnail', blank=True,
                                  default='https://django-music-test-bucket.s3-us-west-2.amazonaws.com/photos/flutter_logo.png')
    song = models.FileField(upload_to='music')

    def __str__(self):
        return f"{self.song.url}"
