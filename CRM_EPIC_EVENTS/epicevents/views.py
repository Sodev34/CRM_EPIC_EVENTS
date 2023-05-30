from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from .serializers import ClientSerializer, ContractSerializer, EventSerializer
from .models import Client, Contract, Event
#from .permissions import ClientPermission, ContractPermission, EventPermission


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]#, ClientPermission]


class ContractViewSet(ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [permissions.IsAuthenticated]#, ContractPermission]


class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]#, EventPermission]
