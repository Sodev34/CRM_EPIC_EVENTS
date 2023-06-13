from rest_framework import viewsets
from rest_framework import permissions
from .models import User, Team, EventStatus
from .serializers import UserSerializer, TeamSerializer, EventStatusSerializer

from .permissions import AccesPermission


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, AccesPermission]


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticated, AccesPermission]


class EventStatusViewSet(viewsets.ModelViewSet):
    queryset = EventStatus.objects.all()
    serializer_class = EventStatusSerializer
    permission_classes = [permissions.IsAuthenticated, AccesPermission]
