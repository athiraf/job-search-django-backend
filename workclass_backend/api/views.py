import json
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from rest_framework.filters import SearchFilter
from workclass_backend.api.models.job import JobModel
from django_filters import CharFilter, FilterSet
from django_filters.rest_framework import DjangoFilterBackend

from workclass_backend.api.serializers import UserSerializer, JobSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated]


class JobFilter(FilterSet):
    company = CharFilter(field_name="company", lookup_expr='icontains')

    class Meta:
        model = JobModel
        fields = ['company']


class JobViewSet(viewsets.ModelViewSet):
    """
    API endpoint - GET only
    """
    permission_classes = [permissions.AllowAny]
    queryset = JobModel.objects.all().order_by('-date')
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_class = JobFilter
    search_fields = ['@company', '@title']
    serializer_class = JobSerializer