from .models import Quiz
from rest_framework import viewsets
from quiz.serializers import QuizSerializer
from rest_framework.permissions import IsAuthenticated

class QuizViewSet(viewsets.ModelViewSet):
    """
    API Quiz
    """
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = (IsAuthenticated, )