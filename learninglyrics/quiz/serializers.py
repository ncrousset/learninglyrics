from .models import Quiz
from rest_framework import serializers

class QuizSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quiz
        fields = ('lyric', 'user', 'date', )