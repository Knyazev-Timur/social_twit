from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView

from users.models import User
# from authentication.permissions import UserIsActivePermission
from users.serializers import UserCreateSerializer, UserListSerializer, UserDetailSerializer, UserUpdateSerializer


class UserCreateView(CreateAPIView):
    model = User
    serializer_class = UserCreateSerializer
    # permission_classes = [AllowAny]


class UsersListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    # permission_classes = [IsAdminUser]


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    # permission_classes = [IsAdminUser | UserOwnerPermission]

class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    # permission_classes = [IsAdminUser]