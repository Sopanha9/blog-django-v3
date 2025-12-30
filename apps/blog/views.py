from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from apps.api.models import Post, Comment
from django.db.models import Q
from django.core.paginator import Paginator


def blog_list(request):
    """Display all public blog posts with optional search and pagination"""
    q = request.GET.get('q', '').strip()
    base_qs = Post.objects.filter(is_public=True)
    if q:
        base_qs = base_qs.filter(
            Q(title__icontains=q)
            | Q(content__icontains=q)
            | Q(tags__icontains=q)
            | Q(category__icontains=q)
            | Q(author__icontains=q)
        )
    
    # Only select necessary fields to reduce data transfer
    posts_list = base_qs.only(
        'id', 'title', 'slug', 'author', 'category', 'featured_image', 
        'date_created', 'date_updated'
    ).order_by('-date_created')
    
    # Pagination: 6 posts per page
    paginator = Paginator(posts_list, 6)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    
    context = {'posts': posts, 'q': q}
    return render(request, 'blog/blog_list.html', context)


def blog_detail(request, slug):
    """Display a single blog post by slug and handle comments"""
    post = get_object_or_404(Post, slug=slug, is_public=True)
    
    # Optimize: Use prefetch_related to avoid N+1 queries
    comments_qs = post.comments.filter(is_approved=True).order_by('-date_created')
    
    try:
        count = int(request.GET.get('c', '3'))
    except ValueError:
        count = 3
    if count < 1:
        count = 3
    
    # Optimize: Cache count to avoid multiple database queries
    total_comments = comments_qs.count()
    shown_comments = list(comments_qs[:count])
    has_more_comments = total_comments > count
    next_count = count + 5
    
    if request.method == 'POST':
        # Handle comment submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        content = request.POST.get('content')
        
        if name and email and content:
            Comment.objects.create(
                post=post,
                name=name,
                email=email,
                content=content
            )
            messages.success(request, 'Your comment has been submitted successfully!')
            return redirect('blog_detail', slug=slug)
        else:
            messages.error(request, 'Please fill in all fields.')
    
    context = {
        'post': post,
        'comments': comments_qs,
        'shown_comments': shown_comments,
        'total_comments': total_comments,
        'has_more_comments': has_more_comments,
        'next_count': next_count,
        'current_count': count,
    }
    return render(request, 'blog/blog_detail.html', context)

