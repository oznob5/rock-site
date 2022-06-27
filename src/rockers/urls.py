from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('addarticle/', add_article, name='add_article'),
    path('feedback/', about, name='feedback'),
    path('login/', login, name='login'),
    path('post/<int:post_id>/', show_post, name='post'),
]
