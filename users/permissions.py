from rest_framework.permissions import BasePermission


class IsActiveUser(BasePermission):
    """Доступ активным пользователям"""

    def has_permission(self, request, view):
        # manager
        if request.user.is_active:
            return True
        else:
            return False


class IsSuperuser(BasePermission):
    """Доступ Администратору"""

    def has_permission(self, request, view):
        # manager
        if request.user.is_superuser:
            return True
