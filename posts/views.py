from django.db import transaction
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from posts.models import Post
from posts.permissions import PostOwnerPermission
from posts.serializers import PostCreateSerializer, PostListSerializer, PostDetailSerializer, PostUpdateSerializer, \
    PostDestroySerializer


class PostCreateView(CreateAPIView):
    model = Post
    serializer_class = PostCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer: PostCreateSerializer):
        with transaction.atomic():
            post = serializer.save()


class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = [AllowAny]


class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = [AllowAny]

class PostUpdateView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostUpdateSerializer
    permission_classes = [IsAdminUser | PostOwnerPermission]

    def pacth(self, request, *args, **kwargs):
        file = request.data.get('images', None)
        images = Post.objects.create(images=file)
        s: PostUpdateSerializer = self.get_serializer(data=request.data)
        if s.is_valid():
            return Response(s.data)
        else:
            return Response(s.errors, status=400)

class PostDeleteView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDestroySerializer
    permission_classes = [IsAdminUser | PostOwnerPermission]


@method_decorator(csrf_exempt, name='dispatch')
class PostImageView(UpdateView):
    model = Post
    fields = ['title', 'text', 'images']
    permission_classes = [IsAdminUser | PostOwnerPermission]

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.images = request.FILES['images']
        self.object.save()

        return JsonResponse({
            'id': self.object.id,
            'title': self.object.title,
            'text': self.object.text,
            'created_at': self.object.created_at,
            'update_at': self.object.update_at,
            'images': self.object.images.url if self.object.images else None
        })
