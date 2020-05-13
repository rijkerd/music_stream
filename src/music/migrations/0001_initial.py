# Generated by Django 3.0.6 on 2020-05-12 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('artist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=200, unique=True)),
                ('album_thumbnail', models.ImageField(upload_to='album')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_name', models.CharField(max_length=200, unique=True)),
                ('genre_thumbnail', models.ImageField(upload_to='genre')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(default='Title', max_length=200, verbose_name='Song name')),
                ('description', models.CharField(default='', max_length=200)),
                ('song_thumbnail', models.ImageField(upload_to='songsImages')),
                ('song_url', models.FileField(upload_to='music')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='music.Album')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='song_creator', to='artist.Artist')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='song_genre', to='music.Genre')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
