from .models import Lyric
from rest_framework import viewsets
from lyrics.serializers import LyricSerializer
from rest_framework.permissions import IsAuthenticated

class LyricViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed
    """
    queryset = Lyric.objects.all()
    serializer_class = LyricSerializer
    permission_classes = (IsAuthenticated, )
