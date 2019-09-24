from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import include
from rest_framework import routers
from rest_framework.authtoken import views
from adventure.api import PlayerViewSet, RoomViewSet
from . import api


# from adventure.api import move

router = routers.DefaultRouter()
router.register('rooms', RoomViewSet)
router.register('currentRoom', PlayerViewSet)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/adv/', include(router.urls)),
    path('api-token-auth', views.obtain_auth_token)
]
