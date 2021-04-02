from django.db.models.fields import DateTimeField
from django.shortcuts import render, redirect
from login.models import DiscordUser
import os
from datetime import datetime, timedelta
# Create your views here.

def home(request):
    if request.method=='POST':
        rangec = request.POST['range']
        hiddenval = request.POST['hidden']
        hiddenval = int(hiddenval)
        current_user = DiscordUser.objects.get(discord_tag=request.user.discord_tag)
        if (int(rangec) > 0):
            current_user.is_session = True
            current_user.session_end = timedelta(seconds=(int(rangec)*30*60))
            current_user.session_end_time = datetime.now() + current_user.session_end
            print(current_user.session_end_time)            

            # current_user.current_session = 
            # print(current_user.current_session)
        
        prev_trees = current_user.trees
        prev_coins = current_user.coins
        prev_dead_trees = current_user.deadtrees
        if (hiddenval < 0):
            print("inside")
            coins = 20*int(rangec)
            new_dead_trees = int(prev_dead_trees) + int(rangec)
            new_coins = int(prev_coins) - int(coins)
            current_user.deadtrees = new_dead_trees
            current_user.coins = new_coins
            current_user.save()
            return redirect(home)
        coins = 25*int(rangec)
        new_trees = int(prev_trees) + int(rangec)
        new_coins = int(prev_coins) + int(coins)
        current_user.trees = new_trees
        current_user.coins = new_coins
        current_user.save()
        return redirect(home)
    params = {}
    if request.user.is_authenticated:
        params = {'loginuser': request.user}
    return render(request, 'main/home.html', params)

def lb(request):
    users = DiscordUser.objects.order_by('-trees', 'deadtrees').all()
    params = {'users': users}
    if request.user.is_authenticated:
        params = {'loginuser': request.user, 'users': users}
    return render(request, 'main/lb.html', params)

def store(request):
    params = {}
    if request.user.is_authenticated:
        params = {'loginuser': request.user}
    return render(request, 'main/store.html', params)

def reset(request):
    if request.user.is_authenticated:
        current_user = DiscordUser.objects.get(discord_tag=request.user.discord_tag)
        current_user.trees = 0
        current_user.deadtrees = 0
        current_user.coins = 0
        current_user.save()
    return redirect(home)
