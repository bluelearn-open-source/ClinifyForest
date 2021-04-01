from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
import requests
from .models import DiscordUser
from main.views import home
import os
from dotenv import load_dotenv
load_dotenv()

oauth2_redirect_url = os.environ.get('OAUTHURL')

def discord_logout(request):
    logout(request)
    return redirect(home)

def discord_login(request):
    if request.user.is_authenticated:
        return redirect(home)
    return redirect(oauth2_redirect_url)

def discord_login_redirect(request):
    code = request.GET.get('code')
    data = exchange_data(code)
    user = data[0]
    guilds = data[1]
    flag = 0
    for ind in guilds:
        for key in ind:
            if (ind["id"] == os.environ.get('CLINIFY_SERVER_ID')):
                flag = 1
    if flag==1:
        discord_user = authenticate(request, user=user)
        login(request, discord_user, backend='login.auth.DiscordAuthenticationBackend')
        return redirect(home)
    return redirect(home)


def exchange_data(code: str):
    data = {
        'client_id': os.environ.get('MY_DISCORD_CLIENT_ID'),
        'client_secret': os.environ.get('MY_DISCORD_CLIENT_SECRET'),
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': os.environ.get('REDIRECT_URI'),
        'scope': 'identify guilds'
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.post('https://discord.com/api/v8/oauth2/token', data=data, headers=headers)
    credentials = response.json()
    access_token = credentials['access_token']
    response = requests.get('https://discord.com/api/v8/users/@me', headers={
        'Authorization': 'Bearer %s' % access_token
    })
    response2 = requests.get('https://discord.com/api/v8/users/@me/guilds', headers={
        'Authorization': 'Bearer %s' % access_token
    })
    guilds = response2.json()
    user = response.json()
    data = [user, guilds]
    return data
