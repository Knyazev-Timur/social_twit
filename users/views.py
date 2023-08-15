
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
# from authentication.permissions import UserIsActivePermission
from users.serializers import UserCreateSerializer, UserListSerializer


class UserCreateView(CreateAPIView):
    model = User
    serializer_class = UserCreateSerializer
    # permission_classes = [AllowAny]


class UsersListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    # permission_classes = [IsAdminUser]