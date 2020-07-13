"""pandoratradingsolution URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.flatpages import views as flatpageview
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from . import views

handler404 = 'pandoratradingsolution.views.handler404'

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('marketdictionary/', include('marketDictionary.urls', namespace='marketDictionary')),
    path('dailyanalysis/', include('dailyAnalysis.urls')),
    path('predictions/', include('predictions.urls')),
    path('admin/', admin.site.urls, name='admin'),
    path('signup/', views.signup, name='signup'),
    #path('login/', auth_views.LoginView.as_view(template_name='pandoratradingsolution/login.html'), name='login'),
path('login/', auth_views.LoginView.as_view(template_name='pandoratradingsolution/page-login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='pandoratradingsolution/logged_out.html'), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('profile/', views.profile_view, name='profile'),
]

if settings.DEBUG:
    if settings.MEDIA_ROOT:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

# flatpages
urlpatterns += [
    path('how-to-use/', flatpageview.flatpage, {'url': '/how-to-use/'}, name='how-to-use'), # страница о том как пользоваться сайтом
    path('how-to-use_elder/', flatpageview.flatpage, {'url': '/how-to-use_elder/'}, name='how-to-use_elder'), # страница о том как пользоваться сайтом
    path('how-to-use_channel/', flatpageview.flatpage, {'url': '/how-to-use_channel/'}, name='how-to-use_channel'), # страница о том как пользоваться сайтом
    path('how-to-use_divbar/', flatpageview.flatpage, {'url': '/how-to-use_divbar/'}, name='how-to-use_divbar'), # страница о том как пользоваться сайтом
    path('how-to-use_volatility/', flatpageview.flatpage, {'url': '/how-to-use_volatility/'}, name='how-to-use_volatility'), # страница о том как пользоваться сайтом
    path('about/', flatpageview.flatpage, {'url': '/about/'}, name='about'),
    path('contact/', flatpageview.flatpage, {'url': '/contact/'}, name='contact'),
]