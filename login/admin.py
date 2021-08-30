from django.contrib import admin
from .models import DiscordUser
from django.contrib.auth.models import Group

# Register your models here.
admin.site.unregister(Group)


@admin.register(DiscordUser)
class DiscordUserAdmin:
    list_display = ("discord_tag", "coins", "trees",
                    "deadtrees", "in_session", "slowmode")
    list_filter = ("discord_tag", "coins", "trees",
                   "deadtrees", "in_session", "slowmode")
    search_fields = ("discord_tag",)
