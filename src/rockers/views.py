from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import *


def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'title': 'Main',
        'role_selected': 0,
        }
    return render(request, 'rockers/index.html', context=context)


def about(request):
    context = {
        'title': 'About Page'
    }
    return render(request, 'rockers/about.html', context=context)


def add_article(request):
    return HttpResponse("Page which adding an article")


def feedback(request):
    return HttpResponse("<h1>Feedback Page</h1>")


def login(request):
    return HttpResponse("<h1>Sign In PAge</h1>")


def show_post(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)

    context = {
        'post': post,
        'title': post.name,
        'role_selected': post.role_id,
    }

    return render(request, 'rockers/post.html', context=context)


def show_role(request, role_slug):
    role = get_object_or_404(Role, slug=role_slug)
    posts = get_list_or_404(Post, role_id=role.id)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'title': 'Main',
        'role_selected': role_slug,
        }
    return render(request, 'rockers/index.html', context=context)
