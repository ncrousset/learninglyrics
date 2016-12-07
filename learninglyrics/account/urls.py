from rest_framework import routers
from account import views
from django.conf.urls import url, include

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]

