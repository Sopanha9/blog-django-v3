from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    title = models.CharField(max_length=200, help_text="Enter the blog post title")
    author = models.CharField(max_length=100, help_text="Author name")

    is_public = models.BooleanField(default=True, help_text="Check to publish this post")
    content = RichTextUploadingField(help_text="Write your blog content here")
    slug = models.SlugField(unique=True, max_length=200, help_text="URL-friendly version of title (auto-filled)")
    featured_image = models.ImageField(upload_to='posts/featured/', blank=True, null=True, help_text="Upload a featured image for this post")
    content = RichTextUploadingField("ខ្លឹមសារ")
    category = models.CharField(max_length=100, default='Uncategorized', help_text="Category of the blog post")
    tags = models.CharField(max_length=200, blank=True, help_text="Comma-separated tags for the post")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_created']
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', help_text="The blog post this comment belongs to")
    name = models.CharField(max_length=100, help_text="Your name")
    email = models.EmailField(help_text="Your email (will not be displayed publicly)")
    content = models.TextField(help_text="Your comment")
    is_approved = models.BooleanField(default=True, help_text="Approve this comment to display publicly")
    date_created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_created']
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
    
    def __str__(self):
        return f'Comment by {self.name} on {self.post.title}'
    
    