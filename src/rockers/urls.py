from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('addarticle/', add_article, name='add_article'),
    path('feedback/', about, name='feedback'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('role/<slug:role_slug>/', show_role, name='role')
]
