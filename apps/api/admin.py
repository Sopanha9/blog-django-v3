from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'is_public', 'date_created', 'date_updated']
    list_filter = ['is_public', 'category', 'date_created', 'author']
    search_fields = ['title', 'content', 'author', 'category', 'tags']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['date_created', 'date_updated']
    list_editable = ['is_public']
    ordering = ['-date_created']
    
    fieldsets = (
        ('Post Content', {
            'fields': ('title', 'featured_image', 'slug', 'author', 'category', 'content', 'tags')
        }),
        ('Settings', {
            'fields': ('is_public',)
        }),
        ('Timestamps', {
            'fields': ('date_created', 'date_updated'),
            'classes': ('collapse',)
        }),
    )
    
    class Media:
        css = {
            'all': ('admin/css/custom_admin.css',)
        }


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'post', 'email', 'is_approved', 'date_created']
    list_filter = ['is_approved', 'date_created']
    search_fields = ['name', 'email', 'content', 'post__title']
    list_editable = ['is_approved']
    readonly_fields = ['date_created']
    ordering = ['-date_created']
    
    fieldsets = (
        ('Comment Info', {
            'fields': ('post', 'name', 'email', 'content')
        }),
        ('Moderation', {
            'fields': ('is_approved', 'date_created')
        }),
    )
