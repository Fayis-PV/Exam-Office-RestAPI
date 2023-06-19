from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    """
    Custom permission to only allow admins to perform write operations.
    Non-admin users have read-only access.
    """

    def has_permission(self, request, view):
        # Allow read-only permissions for all requests
        if request.method in SAFE_METHODS:
            return True

        # Restrict write permissions to admin users only
        return request.user.is_staff


class IsSuperUserOrReadOnly(BasePermission):
    """
    Custom permission to only allow admins to perform write operations.
    Non-admin users have read-only access.
    """

    def has_permission(self, request, view):
        # Allow read-only permissions for all requests
        if request.method in SAFE_METHODS:
            return True

        # Restrict write permissions to admin users only
        return request.user.is_superuser