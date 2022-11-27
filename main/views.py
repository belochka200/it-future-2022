from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import RegForm, PostForm
from django.contrib.auth.models import User

def create_post(request):
    if request.method == 'GET':
        data = {'form': PostForm}
        return render(request, 'create_post.html', context=data)
    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post.objects.create(**form.cleaned_data)
            return redirect(to=post.get_absolute_url())

def reg(request):
    if request.method == 'GET':
        return render(request, 'registration/reg.html')
    elif request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            # Create user
            User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
            )
        return redirect(to='login')

def home(request):
    posts = Post.objects.all()
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
    пост.views += 1
    пост.save(update_fields=['views'])
    данные = {
        'пост': пост,
        'просмотры': пост.views
    }
    return render(request, 'post_detail.html', данные)