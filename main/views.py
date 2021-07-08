from django.db.models.fields import DateTimeField
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from login.models import DiscordUser
from .models import Store, Feed
import os
from datetime import datetime, timedelta
try:
    from ClinifyForest.local_settings import TZC
except:
    pass
# Create your views here.

def setsession(request, rangec):
    if (rangec > 0):
        request.user.in_session = True
        request.user.session_end = timedelta(seconds=(int(rangec)*30*60))
        try:
            if TZC == 0:
                tzcorrection = timedelta(seconds=((int(rangec)*30*60)))
        except:
            tzcorrection = timedelta(seconds=((int(rangec)*30*60) + 19800))
        request.user.session_end_time = datetime.now() + tzcorrection
        request.user.save()
    return redirect(home)

def finalizesession(request, hiddenval, rangec):
    request.user.in_session = False
    request.user.session_end = None
    request.user.session_end_time = None
    if (hiddenval == -1):
        coins = 20*int(rangec)
        new_dead_trees = int(request.user.deadtrees) + int(rangec)
        if int(request.user.coins) < int(coins):
            new_coins = 0
        else:
            new_coins = int(request.user.coins) - int(coins)
        request.user.deadtrees = new_dead_trees
        request.user.coins = new_coins
        request.user.save()
        return redirect(home)
    elif (hiddenval == 0):
        if request.user.slowmode == True:
            coins = 10*int(rangec)
            new_coins = int(request.user.coins) + int(coins)
            request.user.coins = new_coins
            request.user.save()
            return redirect(home)
        coins = 25*int(rangec)
        new_coins = int(request.user.coins) + int(coins)
        request.user.coins = new_coins
        new_trees = int(request.user.trees) + int(rangec)
        request.user.trees = new_trees
        request.user.save()
        return redirect(home)
    else:
        request.user.save()
        return redirect(home)

def home(request):
    feed = Feed.objects.order_by('-timestamp')[:8]
    if request.method=='POST':
        hiddenval = int(request.POST['hidden'])
        rangec = int(request.POST['range'])
        if (request.user.in_session == True):
            finalizesession(request, hiddenval, rangec)
        else:
            setsession(request, rangec)
    params = {'feed':feed}
    return render(request, 'main/home.html', params)

def lb(request):
    users = DiscordUser.objects.order_by('-trees', 'deadtrees')[:50]
    params = {'users': users}
    return render(request, 'main/lb.html', params)

def store(request):
    if request.method=='POST':
        hidden = request.POST['hidden']
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
    return render(request, 'main/store.html', params)

def reset(request):
    if request.user.is_authenticated:
        current_user = DiscordUser.objects.get(discord_tag=request.user.discord_tag)
        current_user.trees = 0
        current_user.deadtrees = 0
        current_user.coins = 0
        current_user.save()
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

def sitemap(request):
    return render(request, 'sitemap.xml', content_type="text/xml")

def getFile(request):
    acmeFile = "gh_tJXTn4rJpdW_d-DISLhisFG5QG380e6gMGqd6QOE.7auUOcRJDGxBFZGXdFcifizjWuT8hvR8Fpm-RT5i-UI"
    return HttpResponse(acmeFile, content_type='text/plain')