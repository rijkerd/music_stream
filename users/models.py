import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(blank=True, max_length=255)
    email = models.EmailField(unique=True, blank=False, error_messages={
        'unique': "A user with that email already exists"
    })

    class Meta:
        ordering = ['last_login']

    def __str__(self):
        return self.email
