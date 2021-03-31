from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
import requests
from login.models import DiscordUser
import os
# Create your views here.

def home(request):
    if request.method=='POST':
        rangec = request.POST['range']
        hiddenval = request.POST['hidden']
        hiddenval = int(hiddenval)
        current_user = DiscordUser.objects.get(discord_tag=request.user.discord_tag)
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
