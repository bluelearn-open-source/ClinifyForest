from django.http import HttpResponse

def getFile(request):
    acmeFile = 'gh_tJXTn4rJpdW_d-DISLhisFG5QG380e6gMGqd6QOE.7auUOcRJDGxBFZGXdFcifizjWuT8hvR8Fpm-RT5i-UI" > /path/to/www/.well-known/acme-challenge/gh_tJXTn4rJpdW_d-DISLhisFG5QG380e6gMGqd6QOE'
    return HttpResponse(acmeFile, content_type='text/plain')
