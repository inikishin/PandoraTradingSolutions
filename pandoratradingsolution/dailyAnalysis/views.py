from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Post


def index(request):
    return HttpResponse("Hello, world. You're at the dailyAnalysis index.")


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'dailyAnalysis/detail.html', {'post': post})