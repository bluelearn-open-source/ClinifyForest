from django.contrib.auth.backends import BaseBackend
from .models import DiscordUser
from django.contrib.auth.models import User

class DiscordAuthenticationBackend(BaseBackend):
    def authenticate(self, request, user) -> DiscordUser:
        find_user = DiscordUser.objects.filter(id=user['id'])
        if (len(find_user) != 0):
            find_user = find_user.first()
            find_user.avatar = user['avatar']
            find_user.discord_tag = '%s#%s' % (user['username'], user['discriminator'])
            find_user.save()
            return find_user
        new_user = DiscordUser.objects.create_new_discord_user(user)
        return new_user

    def get_user(self, user_id):
        try:
            return DiscordUser.objects.get(id=user_id)
        except DiscordUser.DoesNotExist:
            return None