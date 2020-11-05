from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.blog_view, name='blog_view'),
    path('<str:category>', views.category_view, name='category_view'),
    path('<str:category>/<slug:post_slug>', views.post_view, name='post_view')
]