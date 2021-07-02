from rest_framework import serializers
from login.models import DiscordUser
from main.models import Store

class DiscordUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DiscordUser
        fields = ['id','discord_tag', 'avatar', 'trees', 'deadtrees', 'coins', 'level', 'in_session']
