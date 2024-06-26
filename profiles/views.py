from rest_framework import generics, permissions
from .models import Profile, Follow
from .serializers import ProfileSerializer, FollowSerializer
from backend.permissions import IsOwnerOrReadOnly


# Create your views here.


class ProfileListView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProfileDetailView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

class FollowListCreateView(generics.ListCreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(follower=self.request.user)