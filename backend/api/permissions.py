from rest_framework import permissions
from rest_framework.permissions import  BasePermission


class  IsAuthorOrAdminOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        return (
            obj.author == request.user
            or request.method in permissions.SAFE_METHODS
            or request.user.is_superuser)


class IsAdminOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_staff)
