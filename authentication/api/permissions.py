from rest_framework import permissions

class AnonPermissionOnly(permissions.BasePermission):
    message = 'You are already authenticated. Please log out to try again.'

    def has_permission(self, request, view):
        return not request.user.is_authenticated()


class IsOwnerOrReadOnly(permissions.BasePermission):
    message  = 'You must be the user of this content to change.'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
    
        return obj.guest == request.user
