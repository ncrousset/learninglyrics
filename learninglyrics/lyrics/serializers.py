from .models import Lyric, Author, MusicProduction
from rest_framework import serializers

class LyricSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lyric
        fields = ('title', 'context', 'lannguage', 'url_video', 'published',)


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ('name', 'url_avatar',)


class MusicProductionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MusicProduction
        fields = ('title', 'url_cover_page', 'published')
