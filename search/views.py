from django.shortcuts import render
from login.models import DiscordUser

# Create your views here.
def search(request):
    if request.GET:
        query = request.GET['q']
    if len(query)>60 or len(query)<3:
        users = DiscordUser.objects.none()
    else:
        users = DiscordUser.objects.filter(discord_tag__icontains=query)
    params = {'users': users}   
    if request.user.is_authenticated:
        params = {}
        params = {'loginuser': request.user, 'users': users}
    return render(request, 'search/search.html', params)
