from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request

from comments.models import Comment


class CommentOwnerPermission(IsAuthenticated):
    def has_object_permission(self, request: Request, view: GenericAPIView, obj: Comment) -> bool:
        return obj.author.id == request.user.id
