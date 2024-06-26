from django.urls import path
from .views import ProfileListView, ProfileDetailView, FollowListCreateView

urlpatterns = [
    path('', ProfileListView.as_view(), name='profile-list'),
    path('<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),
    path('follows/', FollowListCreateView.as_view(), name='follow-list-create'),
]
