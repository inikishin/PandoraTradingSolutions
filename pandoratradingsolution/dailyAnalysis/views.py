from datetime import datetime
from collections import Counter

from django.shortcuts import render, HttpResponse, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post
import marketDictionary.models as md
import predictions.models as post_model

def index(request):
    filter_post_date = request.GET.get('post_date', '')
    filter_post_ticker = request.GET.get('post_ticker', '')
    filter_post_sig_only = request.GET.get('post_sig_only', '')
    print('GET: post_date: ' + filter_post_date + ' / filter_post_ticker: ' + filter_post_ticker)

    post_list = Post.objects.order_by('-date_analysis')
    if filter_post_sig_only != '':
        post_list = post_list.filter(sig_elder__in=[-1, 1]) | post_list.filter(sig_channel__in=[-1, 1]) | post_list.filter(sig_DivBar__in=[-1, 1]) | post_list.filter(sig_NR4ID__in=[-1, 1]) | post_list.filter(sig_breakVolatility__in=[-1, 1])
    if filter_post_date != '':
        post_list = post_list.filter(date_analysis__range=(datetime.strptime(filter_post_date, '%Y-%m-%d'), datetime.strptime(filter_post_date, '%Y-%m-%d')))
    if filter_post_ticker != '':
        ticker_obj = md.Ticker.objects.filter(short_name=filter_post_ticker).first()
        if ticker_obj != None:
            post_list = post_list.filter(ticker__exact=ticker_obj.id)
        else:
            post_list = post_list.filter(ticker__exact=-1)

    paginator = Paginator(post_list, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'post_date': filter_post_date,
               'post_ticker': filter_post_ticker,
               'page_obj': page_obj}

    return render(request, 'dailyAnalysis/ms_index.html', context)


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    post_all = Post.objects.all().order_by('-date_analysis')
    post_count = len(post_all)
    pred_count = len(post_model.Prediction.objects.all())

    d_list = []
    for p in post_all:
        d_list.append(p.date_analysis.replace(day=1))
    post_counter = list(Counter(d_list).items())

    ticker_list = md.Ticker.objects.all()

    context = {'post': post,
               'post_count': post_count,
               'pred_count': pred_count,
               'post_counter': post_counter,
               'ticker_list': ticker_list}

    return render(request, 'dailyAnalysis/ms_detail.html', context)


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