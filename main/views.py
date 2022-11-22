from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User

def home(request):
    posts = Post.objects.all()
    print(posts)
    context = {
        'posts': posts
    }
    return render(request, "home.html", context)

def test(request):
    print(request.user)
    data = {
        'username': request.user.username,
        'id': request.user.id,
    }
    return render(request, 'user.html', context=data)