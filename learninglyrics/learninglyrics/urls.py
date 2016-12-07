from django.conf.urls import url, include
from rest_framework import routers
from account import views
from django.contrib import admin

router = routers.DefaultRouter()


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('account.urls')),
    url(r'^api/', include('lyrics.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]