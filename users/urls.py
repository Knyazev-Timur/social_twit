from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import UserCreateView, UsersListView, UserDetailView, UserUpdateView, UserDeleteView

urlpatterns = [
    path('create/', UserCreateView.as_view()),
    path('<int:pk>/', UserDetailView.as_view()),
    path('<int:pk>/update/', UserUpdateView.as_view()),
    path('<int:pk>/delete/', UserDeleteView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('', UsersListView.as_view()),
]
