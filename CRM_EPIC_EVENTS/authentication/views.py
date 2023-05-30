from rest_framework import viewsets
from rest_framework import permissions
from .models import User, Team, Statut
from .serializers import UserSerializer, TeamSerializer, StatutSerializer

from .permissions import AccesPermission

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, AccesPermission]

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticated, AccesPermission]

class StatutViewSet(viewsets.ModelViewSet):
    queryset = Statut.objects.all()
    serializer_class = StatutSerializer
    permission_classes = [permissions.IsAuthenticated, AccesPermission]


