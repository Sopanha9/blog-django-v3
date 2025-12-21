from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from apps.api.models import Post, Comment
from django.db.models import Q


def blog_list(request):
    """Display all public blog posts with optional search"""
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
    posts = base_qs.order_by('-date_created')
    context = {'posts': posts, 'q': q}
    return render(request, 'blog/blog_list.html', context)


def blog_detail(request, slug):
    """Display a single blog post by slug and handle comments"""
    post = get_object_or_404(Post, slug=slug, is_public=True)
    comments_qs = post.comments.filter(is_approved=True).order_by('-date_created')
    try:
        count = int(request.GET.get('c', '3'))
    except ValueError:
        count = 3
    if count < 1:
        count = 3
    shown_comments = list(comments_qs[:count])
    total_comments = comments_qs.count()
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

