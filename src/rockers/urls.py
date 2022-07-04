from django.urls import path
from .views import *


urlpatterns = [
    path('', RockHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addarticle/', AddArticleCreateView.as_view(), name='add_article'),
    path('feedback/', about, name='feedback'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', ShowPostDetailView.as_view(), name='post'),
    path('role/<slug:role_slug>/', RockRoleView.as_view(), name='role')
]
