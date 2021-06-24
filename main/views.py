from django.db.models.fields import DateTimeField
from django.http import JsonResponse
from django.shortcuts import render, redirect
from login.models import DiscordUser
from .models import Store
import os
from datetime import datetime, timedelta
try:
    from ClinifyForest.local_settings import TZC
except:
    pass
# Create your views here.

def home(request):
    if request.method=='POST':
        current_user = DiscordUser.objects.get(discord_tag=request.user.discord_tag)
        prev_trees = current_user.trees
        prev_coins = current_user.coins
        prev_dead_trees = current_user.deadtrees
        hiddenval = int(request.POST['hidden'])
        rangec = int(request.POST['range'])
        if (current_user.in_session == True):
            current_user.in_session = False
            current_user.session_end = None
            current_user.session_end_time = None
            if (hiddenval == -1):
                coins = 20*int(rangec)
                new_dead_trees = int(prev_dead_trees) + int(rangec)
                if int(prev_coins) < int(coins):
                    new_coins = 0
                else:
                    new_coins = int(prev_coins) - int(coins)
                current_user.deadtrees = new_dead_trees
                current_user.coins = new_coins
                current_user.save()
                return redirect(home)
            elif (hiddenval == 0):
                if request.user.slowmode == True:
                    coins = 10*int(rangec)
                    new_coins = int(prev_coins) + int(coins)
                    current_user.coins = new_coins
                    current_user.save()
                    return redirect(home)
                coins = 25*int(rangec)
                new_coins = int(prev_coins) + int(coins)
                current_user.coins = new_coins
                new_trees = int(prev_trees) + int(rangec)
                current_user.trees = new_trees
                current_user.save()
                return redirect(home)
            elif (hiddenval == 1):
                current_user.save()
                return redirect(home)
        else:
            if (rangec > 0):
                current_user.in_session = True
                current_user.session_end = timedelta(seconds=(int(rangec)*30*60))
                try:
                    if TZC == 0:
                        tzcorrection = timedelta(seconds=((int(rangec)*30*60)))
                except:
                    tzcorrection = timedelta(seconds=((int(rangec)*30*60) + 19800))
                current_user.session_end_time = datetime.now() + tzcorrection
                current_user.save()
                return redirect(home)
    params = {}
    if request.user.is_authenticated:
        params = {'loginuser': request.user}
    return render(request, 'main/home.html', params)

def lb(request):
    users = DiscordUser.objects.order_by('-trees', 'deadtrees')[:50]
    params = {'users': users}
    if request.user.is_authenticated:
        params = {'loginuser': request.user, 'users': users}
    return render(request, 'main/lb.html', params)

def store(request):
    if request.method=='POST':
        hidden = request.POST['hidden']
        if hidden == "Room Access":
            request.user.room_access = True
            request.user.coins -= 199
            request.user.save()
            return redirect(store)
        if hidden == "Room Admin":
            request.user.room_admin = True
            request.user.coins -= 999
            request.user.save()
            return redirect(store)
        if hidden == "Water Your Trees":
            if request.user.deadtrees == 0:
                return redirect(store)
            request.user.deadtrees -= 1
            request.user.trees += 1
            request.user.coins -= 299
            request.user.save()
            return redirect(store)
    storeitems = Store.objects.all()
    params = {'store': storeitems}
    if request.user.is_authenticated:
        params = {'loginuser': request.user, 'store': storeitems}
    return render(request, 'main/store.html', params)

def reset(request):
    if request.user.is_authenticated:
        current_user = DiscordUser.objects.get(discord_tag=request.user.discord_tag)
        current_user.trees = 0
        current_user.deadtrees = 0
        current_user.coins = 0
        current_user.save()
    return redirect(home)


def rooms(request):
    params = {}
    if request.user.is_authenticated:
        params = {'loginuser': request.user}
        if request.user.room_access:
            return render(request, 'main/rooms.html', params)
        return redirect(home)
    return redirect(home)

def assetlinks(request):
    response_data = [
        {
            "relation": [
                "delegate_permission/common.handle_all_urls"
            ],
            "target": {
                "namespace": "android_app",
                "package_name": "com.herokuapp.clinifyforest.twa",
                "sha256_cert_fingerprints": [
                    "78:57:6E:D0:19:47:29:8A:07:A5:DB:4A:40:50:01:D2:A4:3E:9F:BC:EA:AF:A0:2E:96:CD:C5:F0:99:53:96:D2"
                ]
            }
        }
    ]
    return JsonResponse(response_data, safe=False)