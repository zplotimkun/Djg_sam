from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Post
from .forms import PostForm
# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def add(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(reverse('index'))
    return render(request, 'add.html', {'form' : form})

def delete(request, pk=None):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect(reverse('index'))

def edit(request, pk=None):
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect(reverse('index'))
    return render(request, 'edit.html', 
    {'form': form, 'pk': pk})