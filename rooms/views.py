from django.shortcuts import render, redirect

def index(request):
    return render(request, 'rooms/index.html')

def room(request, room_name):
    print(room_name)
    if room_name == 'monke' or room_name == 'babysloth' or room_name == 'coding':
        return render(request, 'rooms/room.html', {
            'room_name': room_name
        })
    return redirect(index)