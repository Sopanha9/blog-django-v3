from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from django.db.models import Prefetch
from .models import Post, Comment
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    # Add queryset as a class attribute for DRF router
    queryset = Post.objects.none()  # Default empty queryset
    
    def get_queryset(self):
        """Optimize queryset with prefetch_related for comments"""
        # Prefetch approved comments to avoid N+1 queries
        approved_comments = Comment.objects.filter(is_approved=True)
        return Post.objects.filter(is_public=True).prefetch_related(
            Prefetch('comments', queryset=approved_comments)
        ).order_by('-date_created')
