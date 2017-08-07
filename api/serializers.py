from rest_framework import serializers
from posts.models import Post

class PostListSerializer(serializers.ModelSerializer):
	class Meta: 
		model = Post
		fields = ['title', 'author', 'slug', 'content', 'publish']


class PostDetailSerializer(serializers.ModelSerializer):
	class Meta: 
		model = Post
		fields = ['id','title', 'author', 'slug', 'content', 'publish','draft']

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content','draft','publish',]


