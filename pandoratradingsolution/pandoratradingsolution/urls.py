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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from . import views

handler404 = 'pandoratradingsolution.views.handler404'
handler500 = 'pandoratradingsolution.views.handler500'

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('marketdictionary/', include('marketDictionary.urls', namespace='marketDictionary')),
    path('dailyanalysis/', include('dailyAnalysis.urls')),
    path('predictions/', include('predictions.urls')),
    path('admin/', admin.site.urls, name='admin'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='pandoratradingsolution/ms_login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='pandoratradingsolution/logged_out.html'), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('profile/', views.profile_view, name='profile'),
    path('contact/', views.EContactsView.as_view(), name='contact'),
    path('about/', views.about, name='about'),
    path('coming/', views.coming, name='coming'),
    path('search/', views.search, name='search')
]

if settings.DEBUG:
    if settings.MEDIA_ROOT:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

# flatpages
urlpatterns += [
    path('how-to-use/', views.flatpage, {'url': '/how-to-use/'}, name='how-to-use'), # страница о том как пользоваться сайтом
    path('how-to-use_elder/', views.flatpage, {'url': '/how-to-use_elder/'}, name='how-to-use_elder'), # страница о том как пользоваться сайтом
    path('how-to-use_channel/', views.flatpage, {'url': '/how-to-use_channel/'}, name='how-to-use_channel'), # страница о том как пользоваться сайтом
    path('how-to-use_divbar/', views.flatpage, {'url': '/how-to-use_divbar/'}, name='how-to-use_divbar'), # страница о том как пользоваться сайтом
    path('how-to-use_volatility/', views.flatpage, {'url': '/how-to-use_volatility/'}, name='how-to-use_volatility'), # страница о том как пользоваться сайтом
    path('how-to-use_NR4ID/', views.flatpage, {'url': '/how-to-use_nr4id/'}, name='how-to-use_NR4ID'), # страница о том как пользоваться сайтом
]