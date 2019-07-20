# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.
def posts(request):
    posts = Post.objects.all().order_by('date')
    return render(request, 'posts/blogposts.html', {'posts': posts})

def post_detail(request,slug):
    # return HttpResponse(slug)

    post= Post.objects.get(slug=slug)
    return render(request, 'posts/post_detail.html', {'post':post})

@login_required(login_url="/accounts/login/")
def post_create(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            #save form to db
            return redirect("posts:list")
    else:
        form = forms.CreatePost()
    return render(request, 'posts/post_create.html',{'form':form})

