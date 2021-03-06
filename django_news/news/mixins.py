from rest_framework import generics, permissions, mixins, decorators, viewsets


class PermissionViewSetMixin:
    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]