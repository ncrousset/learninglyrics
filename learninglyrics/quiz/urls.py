from rest_framework import routers
from quiz import views
from django.conf.urls import url, include

router = routers.DefaultRouter()
router.register(r'quiz', views.QuizViewSet)
router.register(r'detail-quiz', views.DetailQuizViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]