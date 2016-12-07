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
    created_date = models.DateTimeField(default=timezone.now(), blank=True)
    updated_date = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey('auth.user', on_delete=models.SET_NULL, blank=True, null=True)


class MusicProduction(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title', db_index=True)
    url_cover_page = models.URLField(max_length=100, null=True)
    published = models.DateTimeField(auto_now=False, auto_now_add=False)


class Vocabulary(models.Model):
    lyric = models.ForeignKey(Lyric, on_delete=models.CASCADE)
    detail = models.CharField(max_length=100, verbose_name='Detail')
    url_pronunciation = models.CharField(max_length=100, null=True, blank=True)


class AuthorsHasLyrics(models.Model):
    class Meta:
        unique_together = (('author', 'lyric'), )

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    lyric = models.ForeignKey(Lyric, on_delete=models.CASCADE)

class AuthorsHasProduction(models.Model):
    class Meta:
        unique_together = (('author', 'production'), )

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    production = models.ForeignKey(MusicProduction, on_delete=models.CASCADE)


