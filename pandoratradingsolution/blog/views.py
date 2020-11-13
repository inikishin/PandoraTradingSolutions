from django.shortcuts import render

from .models import Category, Post
from pandoratradingsolution import views as pts_views

# Create your views here.
def blog_view(request):
    cats = Category.objects.all()

    context = {'categories': cats}
    context.update(pts_views.get_navbar_stat())
    return render(request, 'blog/blog.html', context=context)

def category_view(request, category):
    category = Category.objects.get(short_name=category)
    posts = Post.objects.filter(category__short_name=category).order_by('-date_published')

    context = {'category' : category,
               'posts': posts}
    context.update(pts_views.get_navbar_stat())
    return render(request, 'blog/category.html', context=context)

def post_view(request, category, post_slug):
    category = Category.objects.get(short_name=category)
    post = Post.objects.get(slug=post_slug)
    context = {'category': category,
               'post': post}
    context.update(pts_views.get_navbar_stat())
    return render(request, 'blog/article.html', context=context)
