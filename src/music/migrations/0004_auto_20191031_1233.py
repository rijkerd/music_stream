# Generated by Django 2.2.6 on 2019-10-31 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20191031_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='albumName',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='genre',
            name='genreName',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='album',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='music.Album', to_field='albumName'),
        ),
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artist.Artist', to_field='name'),
        ),
        migrations.AlterField(
            model_name='song',
            name='genre',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='music.Genre', to_field='genreName'),
        ),
    ]
