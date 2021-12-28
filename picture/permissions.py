from rest_framework import permissions

class IsOwner(permissions.BasePermission):

    def has_objects_permission(self, request, view, obj):
        return obj.owner == request.user
