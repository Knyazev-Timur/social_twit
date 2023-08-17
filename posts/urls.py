from django.contrib import admin
from django.urls import path

from posts.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, PostImageView

urlpatterns = [
    path('', PostListView.as_view()),
    path('<int:pk>/', PostDetailView.as_view()),
    path('create/', PostCreateView.as_view()),
    path('<int:pk>/update/', PostUpdateView.as_view()),
    path('<int:pk>/delete/', PostDeleteView.as_view()),
    path('<int:pk>/image/', PostImageView.as_view()),
]
