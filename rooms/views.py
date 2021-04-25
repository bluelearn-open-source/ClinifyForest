from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'rooms/index.html', {})


def room(request, room_name):
    return render(request, 'rooms/rooms.html', {
        'room_name': room_name
    })