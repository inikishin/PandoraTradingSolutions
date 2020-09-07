from django.urls import path
# from .views import ArticleDetailView
from django.conf.urls import url
from .views import blog_post

app_name = "article"
urlpatterns = [
    path('blog_post/<slug:slug>/', blog_post, name='blog_post')
]