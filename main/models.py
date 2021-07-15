from django.db import models
from login.models import DiscordUser

# Create your models here.
class Store(models.Model):
    item_name = models.CharField(max_length=100)
    item_price = models.IntegerField()
    item_desc = models.CharField(max_length=200)
    category = models.IntegerField(default=1)
    def __str__(self):
        return self.item_name

class Feed(models.Model):
    user = models.ForeignKey(DiscordUser, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.content