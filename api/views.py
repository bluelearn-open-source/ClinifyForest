from django.http.response import HttpResponse
from django.shortcuts import render
from login.models import DiscordUser
from main.models import Store
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import DiscordUserSerializer
# Create your views here.

class getlb(APIView):
    """
    API pulls the leaderboard
    """
    def get(self, request):
        users = DiscordUser.objects.order_by('-trees', 'deadtrees')[:10]
        serializeduser=DiscordUserSerializer(users, many=True)
        return Response(serializeduser.data)
    
class getlbbynum(APIView):
    """
    API pulls the leaderboard
    """
    def get(self, request, num):
        users = DiscordUser.objects.order_by('-trees', 'deadtrees')[:num]
        serializeduser=DiscordUserSerializer(users, many=True)
        return Response(serializeduser.data)

class getuser(APIView):
    """
    API pulls User Info
    """
    def get(self, request, id):
        user = DiscordUser.objects.get(id=id)
        serializeduser=DiscordUserSerializer(user)
        return Response(serializeduser.data)



