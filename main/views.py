from django.db.models.fields import DateTimeField
from django.shortcuts import render, redirect
from login.models import DiscordUser
from .models import Store
import os
from datetime import datetime, timedelta
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
                new_coins = int(prev_coins) - int(coins)
                current_user.deadtrees = new_dead_trees
                current_user.coins = new_coins
                current_user.save()
                return redirect(home)
            elif (hiddenval == 0):
                coins = 25*int(rangec)
                new_trees = int(prev_trees) + int(rangec)
                new_coins = int(prev_coins) + int(coins)
                current_user.trees = new_trees
                current_user.coins = new_coins
                current_user.save()
                return redirect(home)
            elif (hiddenval == 1):
                current_user.save()
                return redirect(home)
        else:
            if (rangec > 0):
                current_user.in_session = True
                current_user.session_end = timedelta(seconds=(int(rangec)*30*60))
                tzcorrection = timedelta(seconds=((int(rangec)*30*60)))
                current_user.session_end_time = datetime.now() + tzcorrection
                current_user.save()
                return redirect(home)
    params = {}
    if request.user.is_authenticated:
        params = {'loginuser': request.user}
    return render(request, 'main/home.html', params)

def lb(request):
    users = DiscordUser.objects.order_by('-trees', 'deadtrees').all()
    current_trees = 0
    for user in users:
        current_trees += user.trees
    params = { 'trfprt': 1000, 'users': users, 'current_trees': current_trees }
    if request.user.is_authenticated:
        params = {'loginuser': request.user, 'users': users, 'trfprt': 1000, 'current_trees': current_trees}
    return render(request, 'main/lb.html', params)

def store(request):
    storeitems = Store.objects.all()
    if request.method=='POST':
        users = DiscordUser.objects.order_by('-trees', 'deadtrees').all()
        current_trees = 0
        for user in users:
            current_trees += user.trees
        hiddenval = request.POST['hidden']
        item = Store.objects.get(item_name=hiddenval)
        if (item.item_name == "Plant a Real Tree"):
            request.user.gonna_plant_tree = True
            print(request.user.gonna_plant_tree)
            request.user.coins = request.user.coins - 1000
            request.user.gonna_plant_tree_on = 1000 + current_trees
            request.user.save()
            return redirect(store)
    params = { 'store': storeitems }
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
