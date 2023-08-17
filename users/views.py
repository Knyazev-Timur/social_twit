from django.db import transaction
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework.response import Response

from users.models import User
from users.permissions import UserOwnerPermission
from users.serializers import UserCreateSerializer, UserListSerializer, UserDetailSerializer, UserUpdateSerializer, \
    UserDestroySerializer


class UserCreateView(CreateAPIView):
    model = User
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer: UserCreateSerializer) -> None:
        with transaction.atomic():
            user = serializer.save()


class UsersListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [IsAdminUser | IsAuthenticated]


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [IsAdminUser | UserOwnerPermission]


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAdminUser | UserOwnerPermission]

    def pacth(self, request, *args, **kwargs):
        # serializer = Reader.objects.all()
        s: UserUpdateSerializer = self.get_serializer(data=request.data)
        if s.is_valid():
            return Response(s.data)
        else:
            return Response(s.errors, status=400)


class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDestroySerializer
    permission_classes = [IsAdminUser]
