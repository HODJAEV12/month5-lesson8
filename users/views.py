from .models import Users
from .serializers import UsersSerializer
from .pagination import UsersPagination
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets

class UsersViewSets(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    pagination_class = UsersPagination

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name']
    ordering_fields = ['last_name', 'id']
    ordering = ['id']