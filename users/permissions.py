from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request

from users.models import User


class UserOwnerPermission(IsAuthenticated):
    def has_object_permission(self, request: Request, view: GenericAPIView, obj: User) -> bool:
        return obj.id == request.user.id
