from rest_framework import permissions


class AccesPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.team_id == 1
