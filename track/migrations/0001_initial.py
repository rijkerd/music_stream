# Generated by Django 3.0.6 on 2020-06-09 14:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('album', '0001_initial'),
        ('artist', '0001_initial'),
        ('genre', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(default='Title', max_length=200)),
                ('description', models.CharField(default='', max_length=200)),
                ('thumbnail', models.ImageField(upload_to='tracks/images')),
                ('url', models.FileField(upload_to='music')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to='album.Album')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to='artist.Artist')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tracks', to='genre.Genre')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_at'],
                'unique_together': {('album', 'created_at')},
            },
        ),
    ]
