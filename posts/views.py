from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from comments.models import Comment
from comments.serializers import CommentUpdateSerializer, CommentDetailSerializer, CommentListSerializer, \
    CommentDestroySerializer, CommentCreateSerializer
from posts.models import Post
from posts.serializers import PostCreateSerializer, PostListSerializer, PostDetailSerializer, PostUpdateSerializer, \
    PostDestroySerializer


# from authentication.permissions import UserIsActivePermission


class PostCreateView(CreateAPIView):
    model = Post
    serializer_class = PostCreateSerializer
    # permission_classes = [AllowAny]


class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    # permission_classes = [IsAdminUser]


class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    # permission_classes = [IsAdminUser | UserOwnerPermission]

class PostUpdateView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostUpdateSerializer
    # permission_classes = [IsAd

class PostDeleteView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDestroySerializer
    # permission_classes = [IsAdminUser]