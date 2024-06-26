from rest_framework import serializers
from .models import Post, Like, Comment, Tag, PostTag

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user', 'post', 'created_at']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'post', 'content', 'created_at', 'updated_at']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class PostTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostTag
        fields = ['id', 'post', 'tag']
