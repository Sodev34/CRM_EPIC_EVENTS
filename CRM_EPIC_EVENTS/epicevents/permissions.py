from rest_framework import permissions
from .models import Client

class ClientPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.team_id == 3 :
            return request.method in permissions.SAFE_METHODS
        return request.user.team_id == 2