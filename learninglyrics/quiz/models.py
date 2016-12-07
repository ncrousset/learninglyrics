from django.db import models
from django.utils import timezone
from lyrics.models import Lyric

class Quiz(models.Model):
    class Meta:
        unique_together = (('user', 'lyric'), )

    user = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    lyric = models.ForeignKey(Lyric, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now(), blank=True)