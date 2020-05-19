from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dailyAnalysis'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('api/posts/', views.PostView.as_view()),
]