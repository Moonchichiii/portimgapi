from rest_framework import serializers
from .models import Profile, Follow
from django.core.exceptions import ValidationError

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'bio', 'avatar']
        read_only_fields = ['user']

    def validate_avatar(self, value):
        if value.size > 2 * 1024 * 1024:
            raise ValidationError("Avatar file size must be less than 2MB.")
        if not value.name.endswith('.webp'):
            raise ValidationError("Avatar file must be in webp format.")
        return value
        
class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ['id', 'follower', 'following', 'created_at']
