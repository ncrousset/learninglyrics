from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializing all the User
    """
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')
