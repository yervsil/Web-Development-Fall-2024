from rest_framework import serializers
from .models import Post

class PostSerializerV2(serializers.ModelSerializer):
    summary = serializers.CharField(source='content', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'summary', 'author', 'timestamp']
