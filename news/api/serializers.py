from rest_framework import serializers
from ..models import Post, Comment

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'slug',
            'header',
            'author',
            'body',
            'publish',
            'created',
            'updated',
            'status',
            'likes',
            'objects',
            'published',
            'tags',
        )


class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = (
            'id',
            'name',
            'email',
            'body',
            'created',
            'updated',
            'active',
        )