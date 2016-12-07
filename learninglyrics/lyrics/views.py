from .models import Lyric, Author
from rest_framework import viewsets
from lyrics.serializers import LyricSerializer, AuthorSerializer
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