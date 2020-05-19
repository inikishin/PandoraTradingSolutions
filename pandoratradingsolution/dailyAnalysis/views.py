from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Post


def index(request):
    post_list = Post.objects.order_by('date_analysis')
    context = {'post_list': post_list}
    return render(request, 'dailyAnalysis/index.html', context)


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'dailyAnalysis/detail.html', {'post': post})


# API


from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PostSerializer


class PostView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response({"posts": serializer.data})

    def post(self, request):
        post = request.data.get('post')
        # Create an ticker from the above data
        serializer = PostSerializer(data=post)
        if serializer.is_valid(raise_exception=True):
            post_saved = serializer.save()
        return Response({"success": "Post id '{}' created successfully".format(post_saved.id)})