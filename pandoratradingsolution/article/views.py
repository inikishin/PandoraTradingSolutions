from django.shortcuts import render, get_object_or_404
from .models import Article
from account.models import Profile
# Create your views here.
# from django.views.generic import DetailView

# class ArticleDetailView(DetailView):
# 	model = Article
# 	context_object_name = 'articel'
# 	queryset = Article.objects.all()

def blog_post(request, slug):
	article = get_object_or_404(Article, url=slug)
	return render(request, 'blog_post.html', {'article':article} )