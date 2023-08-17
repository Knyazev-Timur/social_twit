from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request

from posts.models import Post


class PostOwnerPermission(IsAuthenticated):
    def has_object_permission(self, request: Request, view: GenericAPIView, obj: Post) -> bool:
        return obj.author.id == request.user.id
