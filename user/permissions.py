from . import models, serializers
from rest_framework import viewsets, status, permissions
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class SubscribedUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.subscribed is True:
            return True
        else:
            return False


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_admin is True:
            return True
        else:
            return False


class IsCustomer(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_customer is True:
            return True
        else:
            return False