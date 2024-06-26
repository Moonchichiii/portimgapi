from django.urls import path
from .views import PostListCreateView, PostDetailView, LikeCreateView, CommentListCreateView, PostSearchView

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('likes/', LikeCreateView.as_view(), name='like-create'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('search/', PostSearchView.as_view(), name='post-search'),
]
