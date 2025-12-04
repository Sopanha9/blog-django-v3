from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from apps.api.models import Post, Comment


def blog_list(request):
    """Display all public blog posts"""
    posts = Post.objects.filter(is_public=True).order_by('-date_created')
    context = {'posts': posts}
    return render(request, 'blog/blog_list.html', context)


def blog_detail(request, slug):
    """Display a single blog post by slug and handle comments"""
    post = get_object_or_404(Post, slug=slug, is_public=True)
    comments = post.comments.filter(is_approved=True).order_by('-date_created')
    
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
        'comments': comments,
    }
    return render(request, 'blog/blog_detail.html', context)

