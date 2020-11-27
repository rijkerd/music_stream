# Generated by Django 3.1.3 on 2020-11-27 11:37

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('genre', '0001_initial'),
        ('album', '0001_initial'),
        ('artist', '0001_initial'),
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
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to='album.album')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to='artist.artist')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tracks', to='genre.genre')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
