from django.db import transaction
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response

from posts.models import Post
from posts.serializers import PostCreateSerializer, PostListSerializer, PostDetailSerializer, PostUpdateSerializer, \
    PostDestroySerializer





class PostCreateView(CreateAPIView):
    model = Post
    serializer_class = PostCreateSerializer
    # permission_classes = [AllowAny]

    def perform_create(self, serializer: PostCreateSerializer) -> None:
        with transaction.atomic():
            post = serializer.save()


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

    def pacth(self, request, *args, **kwargs):
        # serializer = Reader.objects.all()
        s: PostUpdateSerializer = self.get_serializer(data=request.data)
        if s.is_valid():
            return Response(s.data)
        else:
            return Response(s.errors, status=400)

class PostDeleteView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDestroySerializer
    # permission_classes = [IsAdminUser]


@method_decorator(csrf_exempt, name='dispatch')
class PostImageView(UpdateView):
    model = Post
    fields = ['title', 'text', 'images']

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.photo = request.FILES['images']
        self.object.save()

        return JsonResponse({
            'id': self.object.id,
            'title': self.object.name,
            'text': self.object.last_name,
            'created_at': self.object.created_at,
            'update_at': self.object.update_at,
            'images': self.object.photo.url if self.object.photo else None
        })
