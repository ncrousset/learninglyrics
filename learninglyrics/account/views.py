from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic.edit import FormView

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from account.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)



