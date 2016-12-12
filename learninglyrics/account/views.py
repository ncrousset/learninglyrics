from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic.edit import FormView

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from account.serializers import UserSerializer
from account.forms import LoginForm




class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

class LoginView(FormView):
    template_name = 'account/login.html'
    form_class = LoginForm
    success_url = '/api/'

    def form_valid(self, form):
        form.start_session()
        return super(LoginView, self).form_valid(form)


