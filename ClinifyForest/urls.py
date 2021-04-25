"""ClinifyForest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main.views import home, lb, store, reset, rooms
from login.views import discord_logout, discord_login, discord_login_redirect
from search.views import search

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name="home"),
    path('', include('pwa.urls')),
    path('leaderboard', lb, name="lb"),
    path('store', store, name="store"),
    path('rooms/', include('rooms.urls')),
    path('reset', reset, name="reset"),
    path('search', search, name="search"),
    path('login', discord_login, name='discord_login'),
    path('logout', discord_logout, name='discord_logout'),
    path('login/redirect', discord_login_redirect, name='discord_login_redirect'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
