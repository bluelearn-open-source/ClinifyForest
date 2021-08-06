from django.http.response import HttpResponse
from django.shortcuts import render
from login.models import DiscordUser
from main.models import Store, Feed
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import DiscordUserSerializer, BackupStoreApiSerializer, BackupUserApiSerializer, BackupFeedApiSerializer
# Create your views here.

class backupusr(APIView):
    """
    API is used to get data when backup is needed
    """
    def get(self, request):
        data = BackupUserApiSerializer(DiscordUser.objects.all(), many=True).data
        return Response(data)

class backupstr(APIView):
    """
    API is used to get data when backup is needed
    """
    def get(self, request):
        data = BackupStoreApiSerializer(Store.objects.all(), many=True).data
        return Response(data)

class backupfed(APIView):
    """
    API is used to get data when backup is needed
    """
    def get(self, request):
        data = BackupFeedApiSerializer(Feed.objects.all(), many=True).data
        return Response(data)

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
        try:
            user = DiscordUser.objects.get(id=id)
            serializeduser=DiscordUserSerializer(user)
            return Response(serializeduser.data)
        except:
            return Response({'error':'User Not Found'})



