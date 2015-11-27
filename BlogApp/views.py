# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__isnull=False).order_by('-published_date')
    return render(request, 'BlogApp/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'BlogApp/post_detail.html', {'post': post})

def post_new(request):
    form = PostForm()
    return render(request, 'BlogApp/post_edit.html', {'form': form})


