from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from comments.models import Comment
from comments.permissions import CommentOwnerPermission
from comments.serializers import CommentUpdateSerializer, CommentDetailSerializer, CommentListSerializer, \
    CommentDestroySerializer, CommentCreateSerializer



class CommentCreateView(CreateAPIView):
    model = Comment
    serializer_class = CommentCreateSerializer
    permission_classes = [IsAuthenticated]


class CommentListView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer
    permission_classes = [AllowAny]


class CommentDetailView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer
    permission_classes = [AllowAny]


class CommentUpdateView(UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentUpdateSerializer
    permission_classes = [IsAdminUser | CommentOwnerPermission]


class CommentDeleteView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDestroySerializer
    permission_classes = [IsAdminUser | CommentOwnerPermission]
