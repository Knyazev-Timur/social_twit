from django.db import transaction
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
# from authentication.permissions import UserIsActivePermission
from users.serializers import UserCreateSerializer, UserListSerializer, UserDetailSerializer, UserUpdateSerializer, \
    UserDestroySerializer

# class BoardCreateViews(generics.CreateAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = BoardSerializer
#
#     def perform_create(self, serializer: BoardSerializer) -> None:
#         with transaction.atomic():
#             board = serializer.save()
#             BoardParticipant.objects.create(user=self.request.user, board=board, role=BoardParticipant.Role.owner)





class UserCreateView(CreateAPIView):
    model = User
    serializer_class = UserCreateSerializer
    # permission_classes = [AllowAny]

    def perform_create(self, serializer: UserCreateSerializer) -> None:
        with transaction.atomic():
            user = serializer.save()





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
    # permission_classes = [IsAdminUser]