from rest_framework import routers
from quiz import views
from django.conf.urls import url, include

router = routers.DefaultRouter()

urlpatterns = [
    url(r'^', include(router.urls)),
]