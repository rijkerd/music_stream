# Generated by Django 3.0.6 on 2020-05-13 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0002_auto_20200513_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True),
        ),
    ]