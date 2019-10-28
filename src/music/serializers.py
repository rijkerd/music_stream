from rest_framework import serializers
from .models import Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('audio_id', 'title', 'description',
                  'thumbnail', 'created_at', 'song')
