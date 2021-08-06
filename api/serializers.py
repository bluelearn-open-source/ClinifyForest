from rest_framework import serializers
from login.models import DiscordUser
from main.models import Store, Feed

class DiscordUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DiscordUser
        fields = ['id','discord_tag', 'avatar', 'trees', 'deadtrees', 'coins', 'level', 'in_session']

class BackupUserApiSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DiscordUser
        fields = ['id', 'discord_tag', 'avatar', 'level', 'coins', 'trees', 'deadtrees', 'in_session', 'session_end', 'session_end_time', 'slowmode', 'public_flags', 'flags', 'locale', 'mfa_enabled', 'last_login']

class BackupStoreApiSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'item_name', 'item_price', 'item_desc', 'category']

class BackupFeedApiSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Feed
        fields = ['id', 'user_id', 'content', 'timestamp']