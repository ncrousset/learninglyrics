from django.db import models
from django.utils import timezone

class Lyric(models.Model):

    MAYBELANGUAGE = (
        ('es', 'espaniol'),
        ('en', 'ingles'),
    )

    title = models.CharField(max_length=100, verbose_name='Title', db_index=True)
    context = models.TextField()
    lannguage = models.CharField(max_length=2, choices=MAYBELANGUAGE, default='en')
    url_video = models.URLField(max_length=200, null=True)
    published = models.DateTimeField(auto_now=False, auto_now_add=False)
    created_date = models.DateTimeField(default=timezone.now(), blank=True)
    updated_date = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey('auth.user', on_delete=models.SET_NULL, blank=True, null=True)


class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name="Author", db_index=True)
    url_avatar = models.URLField(max_length=200, null=True)


