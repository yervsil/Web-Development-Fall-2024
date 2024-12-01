from rest_framework import viewsets
from .models import Post
from .serializers_v2 import PostSerializerV2

class PostViewSetV2(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializerV2
