from rest_framework import routers
from lyrics import views
from django.conf.urls import url, include

router = routers.DefaultRouter()
router.register(r'lyrics', views.LyricViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
