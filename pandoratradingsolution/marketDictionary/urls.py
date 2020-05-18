from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='marketDictionaryIndex'),
    path('<int:ticker_id>/', views.detail, name='detail'),
]