from rest_framework import permissions


class ClientPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        team_id = request.user.team_id

        if team_id == 1:
            return True
        elif team_id == 2 and request.method in ["GET", "POST", "PUT"]:
            return True
        elif team_id == 3 and request.method in permissions.SAFE_METHODS:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if request.user.team_id == 1:
            return True
        elif request.method in permissions.SAFE_METHODS:
            return True
        elif obj.sales_contact == request.user:
            return True
        else:
            return False


class ContractPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        team_id = request.user.team_id

        if team_id == 1:
            return True
        elif team_id == 2 and request.method in ["GET", "POST", "PUT"]:
            return True
        elif team_id == 3 and request.method in permissions.SAFE_METHODS:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if request.user.team_id == 1:
            return True
        elif request.method in permissions.SAFE_METHODS:
            return True
        elif obj.sales_contact == request.user:
            return True
        else:
            return False


class EventPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        team_id = request.user.team_id

        if team_id == 1:
            return True
        elif team_id == 2 and request.method in ["GET", "POST"]:
            return True
        elif team_id == 3 and request.method in ["GET", "PUT"]:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if request.user.team_id == 1:
            return True
        elif request.method in permissions.SAFE_METHODS:
            return True
        elif obj.support_contact == request.user or obj.sales_contact == request.user:
            return True
        else:
            return False
