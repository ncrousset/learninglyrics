from .models import Quiz, DetailQuiz
from rest_framework import serializers

class QuizSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quiz
        fields = ('lyric', 'user', 'date', )

class DetailQuizSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DetailQuiz
        fields = ('quiz', 'vocabulary', 'correct', )