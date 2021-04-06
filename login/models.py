from django.db import models
from .managers import DiscordUserOAuth2Manager

# Create your models here.

class DiscordUser(models.Model):
    objects = DiscordUserOAuth2Manager()

    id = models.BigIntegerField(primary_key=True ,unique=True)
    discord_tag = models.CharField(max_length=100)
    avatar = models.CharField(null=True, max_length=100, blank=True)

    coins = models.IntegerField(default=0)
    trees = models.IntegerField(default=0)
    deadtrees = models.IntegerField(default=0)
    room_admin = models.BooleanField(default=False)
    room_access = models.BooleanField(default=False)
    in_session = models.BooleanField(default=False)
    session_end = models.DurationField(blank=True, null=True)
    session_end_time = models.DateTimeField(blank=True, null=True)
    
    public_flags = models.IntegerField()
    flags = models.IntegerField()
    locale = models.CharField(max_length=100)
    mfa_enabled = models.BooleanField()
    
    last_login = models.DateTimeField(null=True)

    def is_authenticated(self, requet):
        return True

    def __str__(self):
        return self.discord_tag