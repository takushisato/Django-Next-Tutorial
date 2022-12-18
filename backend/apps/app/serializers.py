from rest_framework import serializers
from .models import Post
from apps.account.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'user', 'title', 'iamge', 'content', 'created_at')