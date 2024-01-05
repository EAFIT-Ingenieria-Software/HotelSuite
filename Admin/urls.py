from django.urls import path
from .views import index, RoomManager

urlpatterns = [
    path('', index, name='index'),

    path('rooms/', RoomManager.index, name='room_manager_index'),
]
