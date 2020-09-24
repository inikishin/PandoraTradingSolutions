from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dailyAnalysis'),
    path('<slug:post_slug>/', views.detail_slug, name='detail'),
    path('api/posts/', views.PostView.as_view()),
]