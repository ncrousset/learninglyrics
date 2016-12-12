from django.db import models
from django.utils import timezone
from lyrics.models import Lyric, Vocabulary

class Quiz(models.Model):
    class Meta:
        unique_together = (('user', 'lyric'), )

    user = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    lyric = models.ForeignKey(Lyric, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now(), blank=True)

class DetailQuiz(models.Model):
    class Meta:
        unique_together = (('quiz', 'vocabulary'), )

    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    vocabulary = models.ForeignKey(Vocabulary, on_delete=models.CASCADE)
    correct = models.BooleanField()