from django.shortcuts import render, get_object_or_404
from .models import Article
from account.models import Profile

def blog_post(request, slug):
	article = get_object_or_404(Article, url=slug)
	return render(request, 'blog_post.html', {'article':article} )