from django.urls import path
from . import views

app_name = "tickers"
# app_name will help us do a reverse look-up latter.

urlpatterns = [
    path('', views.index, name='marketDictionary'),
    #path('<int:ticker_id>/', views.detail, name='detail'),
    path('<str:ticker_name>/', views.detail_slug, name='detail'),
    path('api/tickers/', views.TickerView.as_view()),
]