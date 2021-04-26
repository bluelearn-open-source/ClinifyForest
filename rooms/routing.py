from django.conf.urls import url
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    url(r'wss/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer.as_asgi()),
]