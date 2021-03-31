from django.contrib.auth.backends import BaseBackend
from .models import DiscordUser
from django.contrib.auth.models import User

class DiscordAuthenticationBackend(BaseBackend):
    def authenticate(self, request, user) -> DiscordUser:
        find_user = DiscordUser.objects.filter(id=user['id'])
        if (len(find_user) != 0):
            return find_user.first()
        new_user = DiscordUser.objects.create_new_discord_user(user)
        return new_user

    def get_user(self, user_id):
        try:
            return DiscordUser.objects.get(id=user_id)
        except DiscordUser.DoesNotExist:
            return None