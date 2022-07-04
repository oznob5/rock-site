from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView

from .models import *
from .forms import *


class RockHome(ListView):
    model = Post
    template_name = 'rockers/index.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Main'
        context["role_selected"] = 0
        return context
    
    def get_queryset(self):
        return Post.objects.filter(is_published=True)
    

# def index(request):
#     posts = Post.objects.all()
#     context = {
#         'posts': posts,
#         'title': 'Main',
#         'role_selected': 0,
#         }
#     return render(request, 'rockers/index.html', context)


def about(request):
    context = {
        'title': 'About Page'
    }
    return render(request, 'rockers/about.html', context)


class AddArticleCreateView(CreateView):
    form_class = AddPostForm
    template_name = "rockers/add_article.html"
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Add an article'
        return context
    


# def add_article(request):
#     if request.method == "POST":
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()  # sql save
#             return redirect('home')
#     else:
#         form = AddPostForm()

#     context = {
#         'form': form,
#         'title': 'Add an article'
#     }
#     return render(request, 'rockers/add_article.html', context)


def feedback(request):
    return HttpResponse("<h1>Feedback Page</h1>")


def login(request):
    return HttpResponse("<h1>Sign In PAge</h1>")


class ShowPostDetailView(DetailView):
    model = Post
    template_name = "rockers/post.html"
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = context['post']
        return context
    


# def show_post(request, post_slug):
#     post = get_object_or_404(Post, slug=post_slug)

#     context = {
#         'post': post,
#         'title': post.name,
#         'role_selected': post.role_id,
#     }

#     return render(request, 'rockers/post.html', context)


class RockRoleView(ListView):
    model = Post
    template_name = "rockers/index.html"
    context_object_name = 'posts'
    allow_empty = False  # raise 404

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = context['posts'][0].role
        context["role_selected"] =  context['posts'][0].role_id
        return context
    

    def get_queryset(self):
        return Post.objects.filter(role__slug=self.kwargs['role_slug'], is_published=True)
    


# def show_role(request, role_slug):
#     role = get_object_or_404(Role, slug=role_slug)
#     posts = get_list_or_404(Post, role_id=role.id)

#     if len(posts) == 0:
#         raise Http404()

#     context = {
#         'posts': posts,
#         'title': 'Main',
#         'role_selected': role_slug,
#         }
#     return render(request, 'rockers/index.html', context)
