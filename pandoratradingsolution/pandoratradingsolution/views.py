from django.shortcuts import render
from dailyAnalysis.models import Post

def mainpage(request):
    post_list = Post.objects.order_by('-date_analysis')[:30]

    context = {'post_list': post_list}

    return render(request, 'pandoratradingsolution/index.html', context)

def handler404(request, exception):
    return render(request, 'pandoratradingsolution/error404.html', status=404)