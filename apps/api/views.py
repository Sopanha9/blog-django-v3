from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(is_public=True)
    serializer_class = PostSerializer
