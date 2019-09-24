from django.conf.urls import url
from . import api
from adventure.api import RoomViewSet

urlpatterns = [
    url('init', api.initialize),
    url('move', api.move),
    url('say', api.say),
    url('rooms', RoomViewSet)
]