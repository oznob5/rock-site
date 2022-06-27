from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import *


menu = [{'title': 'About', 'url_name': 'about'},
        {'title': 'Add an article', 'url_name': 'add_article'},
        {'title': 'Feedback', 'url_name': 'feedback'},]


def index(request):
    posts = Post.objects.all()
    roles = Role.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'roles': roles,
        'title': 'Main',
        'role_selected': 0,
        }
    return render(request, 'rockers/index.html', context=context)


def about(request):
    context = {
        'menu': menu,
        'title': 'About Page'
    }
    return render(request, 'rockers/about.html', context=context)


def add_article(request):
    return HttpResponse("Page which adding an article")


def feedback(request):
    return HttpResponse("<h1>Feedback Page</h1>")


def login(request):
    return HttpResponse("<h1>Sign In PAge</h1>")


def show_post(request, post_id):
    return HttpResponse(f"Article with id number = {post_id}")


def show_role(request, role_id):
    posts = Post.objects.filter(role_id=role_id)
    roles = Role.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'menu': menu,
        'roles': roles,
        'title': 'Main',
        'role_selected': role_id,
        }
    return render(request, 'rockers/index.html', context=context)
