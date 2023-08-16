from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from comments.models import Comment
from comments.serializers import CommentUpdateSerializer, CommentDetailSerializer, CommentListSerializer, \
    CommentDestroySerializer, CommentCreateSerializer


# from authentication.permissions import UserIsActivePermission


class CommentCreateView(CreateAPIView):
    model = Comment
    serializer_class = CommentCreateSerializer
    # permission_classes = [AllowAny]


class CommentListView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer
    # permission_classes = [IsAdminUser]


class CommentDetailView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer
    # permission_classes = [IsAdminUser | UserOwnerPermission]

class CommentUpdateView(UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentUpdateSerializer
    # permission_classes = [IsAd

class CommentDeleteView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDestroySerializer
    # permission_classes = [IsAdminUser]