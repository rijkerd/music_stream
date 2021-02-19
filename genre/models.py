import uuid
from django.db import models
from core.storage_backends import PublicMediaStorage


class Genre(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, unique=True, blank=False)
    thumbnail = models.FileField(storage=PublicMediaStorage(), blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.name
