from django.conf.urls import url, include
from rest_framework import routers
from django.contrib import admin

router = routers.DefaultRouter()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('account.urls')),
    url(r'^api/', include('lyrics.urls')),
    url(r'^api/', include('quiz.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]