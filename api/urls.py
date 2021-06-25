from django.urls import path
from . import views
from rest_framework import routers

urlpatterns = [
    path('getlb', views.getlb.as_view()),
    path('getuser/<int:id>', views.getuser.as_view()),
    path('getlb/<int:num>', views.getlbbynum.as_view()),
]
