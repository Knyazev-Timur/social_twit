from rest_framework.generics import GenericAPIView
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework.request import Request

from users.models import User


class UserIsActivePermission(BasePermission):
    message = "User is not active!"

    def has_permission(self, request, view):
        if request.user.is_active:
            return True
        else:
            return False


class UserIsActivePermission(BasePermission):
    message = "User is not active!"

    def has_permission(self, request, view):
        if request.user.is_active:
            return True
        else:
            return False



class UserOwnerPermission(IsAuthenticated):
    def has_object_permission(self, request: Request, view: GenericAPIView, obj: User) -> bool:
        return obj.user.id == request.user.id
