from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Post


def index(request):
    post_list = Post.objects.order_by('date_analysis')
    context = {'post_list': post_list}
    return render(request, 'dailyAnalysis/index.html', context)


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'dailyAnalysis/detail.html', {'post': post})