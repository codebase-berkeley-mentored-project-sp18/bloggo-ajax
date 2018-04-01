# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Post

# Create your views here.

def index(request):
    posts = Post.objects.order_by("-pub_date")
    return render(request, "posts/index.html", {"posts": posts})

def about(request):
    return render(request, "posts/about.html")

def post_details(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, "posts/details.html", {"post": post})
