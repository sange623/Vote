from rest_framework import viewsets
from .models import  User,PoleHaveOptions,PoleTable,Vote
from .serializers import UserSerializer,PoleHaveOptionsSerializer,PoleTableSerializer,VoteSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter,DjangoFilterBackend,OrderingFilter]
    search_fields = ['id', 'name']


class PoleHaveOptionsViewset(viewsets.ModelViewSet):
    queryset = PoleHaveOptions.objects.all()
    serializer_class = PoleHaveOptionsSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter,DjangoFilterBackend,OrderingFilter]
    search_fields = ['id']


class PoleTableViewset(viewsets.ModelViewSet):
    queryset = PoleTable.objects.all()
    serializer_class = PoleTableSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter,DjangoFilterBackend,OrderingFilter]
    search_fields = ['id']


class VoteViewset(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter,DjangoFilterBackend,OrderingFilter]
    search_fields = ['id']

    # def get_serializer(self):
    #     if self.action in ['create','update','partial_update']:
    #         return 
    #     return 
    
    
    # def get_queryset(self):
    #     return super().get_queryset()

