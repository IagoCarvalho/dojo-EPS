from rest_framework import serializers
from posts.models import Post
from django.contrib.auth.models import User


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        author = serializers.ReadOnlyField(source='author.username')
        fields = ('creation_date', 'title', 'content', 'author')


class UserSerializer(serializers.ModelSerializer):

    posts = serializers.PrimaryKeyRelatedField(many=True,
                                               queryset=Post.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'posts')
