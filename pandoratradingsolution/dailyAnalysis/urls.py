from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dailyAnalysis'), # TODO: delete after redirect
    path('moex/', views.index, name='dailyAnalysis'),
    path('moex/page<int:page_num>', views.index, name='dailyAnalysis'),
    path('<slug:post_slug>/', views.detail_slug, name='detail'),
    path('api/posts/', views.PostView.as_view()),
]