from rest_framework import routers
from lyrics import views
from django.conf.urls import url, include

router = routers.DefaultRouter()
router.register(r'lyrics', views.LyricViewSet)
router.register(r'authors', views.AuthorViewSet)
router.register(r'music-production', views.MusicProductionViewSet)
router.register(r'vocabulary', views.VocabularyViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
