from rest_framework.permissions import BasePermission


class IsAuthor:
    def has_object_permission(self, request, view, obj):
        pass
