

from rest_framework.permissions import BasePermission

class IsAdminOrManager(BasePermission):
    def has_permission(self, request, view):
        role = request.META.get('X-User-Role')  # Extracted from middleware
        return role in ['admin', 'project_manager']

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        role = request.META.get('X-User-Role')
        return role == 'admin'

class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return 'X-User-UUID' in request.META
