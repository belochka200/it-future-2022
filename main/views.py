from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.models import User

def home(request):
    posts = Post.objects.all()
    print(posts)
    data = {
        'posts': posts
    }
    return render(request, "home.html", data)

def test(request):
    print(request.user)
    data = {
        'username': request.user.username,
        'id': request.user.id,
    }
    return render(request, 'user.html', context=data)

def показать_пост(request, pk):
    пост = get_object_or_404(Post, pk=pk)
    данные = {
        'пост': пост
    }
    return render(request, 'post_detail.html', данные)