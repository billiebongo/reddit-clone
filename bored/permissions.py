#
import logging

logger = logging.getLogger(__name__)

from rest_framework import permissions

class IsUserOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        if (request.user.username==obj.username) and request.method == 'PATCH':
            return True
        if (request.user.is_staff):
            return True
        return False

    def has_permission(self, request, view):
        if view.action == 'list':
            return request.user.is_staff
        if request.user.is_staff:
            return True
        if (request.method == 'PATCH') or (request.method in permissions.SAFE_METHODS):
            return True
        return False
