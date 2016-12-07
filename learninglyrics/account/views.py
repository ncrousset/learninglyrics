from django.contrib.auth.models import User
from rest_framework import viewsets

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from account.serializers import UserSerializer

from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
