"""django_posts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from posts import views as posts_views


urlpatterns = [
    path('admin/', admin.site.urls),

    # Для POSTS
    path('', posts_views.home, name='home'),
    path('about/', posts_views.about, name='about'),
    path('posts/<int:post_id>', posts_views.post),
    path('posts/<post_id>', posts_views.post_str),
    re_path(r'posts/\d+/<post_id>', posts_views.post),
    path('post/create', posts_views.create_post, name='create_post')

]