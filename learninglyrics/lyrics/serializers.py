from .models import Lyric
from rest_framework import serializers

class LyricSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lyric
        fields = ('title', 'context', 'lannguage', 'url_video', 'published',)
