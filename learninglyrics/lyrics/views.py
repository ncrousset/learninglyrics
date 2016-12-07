from .models import Lyric, Author, MusicProduction, Vocabulary
from rest_framework import viewsets
from lyrics.serializers import LyricSerializer, AuthorSerializer, MusicProductionSerializer, VocabularySerializer
from rest_framework.permissions import IsAuthenticated

class LyricViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed
    """
    queryset = Lyric.objects.all()
    serializer_class = LyricSerializer
    permission_classes = (IsAuthenticated, )


class AuthorViewSet(viewsets.ModelViewSet):
    """
    API view de authores
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsAuthenticated, )


class MusicProductionViewSet(viewsets.ModelViewSet):
    """
    API prodicciones musicales
    """
    queryset = MusicProduction.objects.all()
    serializer_class = MusicProductionSerializer
    permission_classes = (IsAuthenticated, )

class VocabularyViewSet(viewsets.ModelViewSet):
    """
    API vocabulary de lyrics
    """
    queryset = Vocabulary.objects.all()
    serializer_class = VocabularySerializer
    permission_classes = (IsAuthenticated, )

