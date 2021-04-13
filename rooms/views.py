from django.shortcuts import render, redirect

def index(request):
    params = {}
    if request.user.is_authenticated:
        params = {'loginuser': request.user}
    return render(request, 'rooms/index.html', params)

def room(request, room_name):
    params = {}
    if request.user.is_authenticated:
        params = {'loginuser': request.user, 'room_name': room_name}
        if room_name == 'padhai-moment' or room_name == 'coding-shoding' or room_name == 'chamber-of-secrets':
            if not request.user.room_admin and room_name == 'chamber-of-secrets':
                return redirect(index)
            return render(request, 'rooms/room.html', params)
    return redirect(index)

