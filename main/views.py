
from django.shortcuts import render
from django.http import HttpResponse
from apps.api.models import Post


# Create your views here.

def home(request):
    posts = Post.objects.all().order_by('-date_created')
    return render(request, 'index.html', {'posts': posts})