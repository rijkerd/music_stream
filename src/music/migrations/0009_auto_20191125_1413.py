# Generated by Django 2.2.6 on 2019-11-25 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0008_auto_20191125_1218'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='albumName',
            new_name='album_name',
        ),
        migrations.RenameField(
            model_name='genre',
            old_name='genreName',
            new_name='genre_name',
        ),
    ]