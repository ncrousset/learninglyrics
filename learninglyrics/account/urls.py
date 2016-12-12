
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

app_name = 'account'

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^accounts/login/$', auth_views.login, {'template_name': 'account/login.html'}, name='account:login', ),
    url(r'^accounts/logout/$', auth_views.logout, {'next_page': '/accounts/login'}),
    url(r'^login/', views.LoginView.as_view(), name='login2'),
]

