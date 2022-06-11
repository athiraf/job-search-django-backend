from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models.job import JobModel


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JobModel
        fields = ['job_id', 'company','title','logo_url','date']