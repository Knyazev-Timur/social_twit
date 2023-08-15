from django.urls import path
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import UserCreateView, UsersListView

urlpatterns = [
    path('create/', UserCreateView.as_view()),
    # path('token/', TokenObtainPairView.as_view()),
    # path('token/refresh/', TokenRefreshView.as_view()),
    path('list/', UsersListView.as_view()),

]

