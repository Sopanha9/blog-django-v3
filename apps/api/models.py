from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    title = models.CharField(max_length=200, help_text="Enter the blog post title", db_index=True)
    author = models.CharField(max_length=100, help_text="Author name", db_index=True)
    is_public = models.BooleanField(default=True, help_text="Check to publish this post", db_index=True)
    slug = models.SlugField(unique=True, max_length=200, help_text="URL-friendly version of title (auto-filled)")
    featured_image = models.ImageField(upload_to='posts/featured/', blank=True, null=True, help_text="Upload a featured image for this post")
    content = RichTextUploadingField("ខ្លឹមសារ", help_text="Write your blog content here")
    category = models.CharField(max_length=100, default='Uncategorized', help_text="Category of the blog post", db_index=True)
    tags = models.CharField(max_length=200, blank=True, help_text="Comma-separated tags for the post")
    date_created = models.DateTimeField(auto_now_add=True, db_index=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_created']
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'
        indexes = [
            models.Index(fields=['-date_created'], name='post_date_created_idx'),
            models.Index(fields=['is_public', '-date_created'], name='post_public_date_idx'),
            models.Index(fields=['category', '-date_created'], name='post_cat_date_idx'),
        ]

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', help_text="The blog post this comment belongs to", db_index=True)
    name = models.CharField(max_length=100, help_text="Your name")
    email = models.EmailField(help_text="Your email (will not be displayed publicly)")
    content = models.TextField(help_text="Your comment")
    is_approved = models.BooleanField(default=True, help_text="Approve this comment to display publicly", db_index=True)
    date_created = models.DateTimeField(auto_now_add=True, db_index=True)
    
    class Meta:
        ordering = ['-date_created']
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        indexes = [
            models.Index(fields=['post', 'is_approved', '-date_created'], name='comment_post_approved_idx'),
        ]
    
    def __str__(self):
        return f'Comment by {self.name} on {self.post.title}'
    
    