from django.urls import path

from comments.views import CommentCreateView, CommentDeleteView, CommentListView, CommentDetailView, CommentUpdateView

urlpatterns = [
    path('', CommentListView.as_view()),
    path('<int:pk>/', CommentDetailView.as_view()),
    path('create/', CommentCreateView.as_view()),
    path('<int:pk>/update/', CommentUpdateView.as_view()),
    path('<int:pk>/delete/', CommentDeleteView.as_view()),
]
