from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='predictions'),
    path('moex/', views.index, name='predictions'),
    path('api/predictions/', views.PredictionView.as_view()),
    path('api/predictionhorizons/', views.PredictionHorizonView.as_view()),
]