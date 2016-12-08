from .models import Quiz, DetailQuiz
from rest_framework import viewsets
from quiz.serializers import QuizSerializer, DetailQuizSerializer
from rest_framework.permissions import IsAuthenticated

class QuizViewSet(viewsets.ModelViewSet):
    """
    API Quiz
    """
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = (IsAuthenticated, )

class DetailQuizViewSet(viewsets.ModelViewSet):
    """
    API Detail quiz
    """
    queryset = DetailQuiz.objects.all()
    serializer_class = DetailQuizSerializer
    permission_classes = (IsAuthenticated, )