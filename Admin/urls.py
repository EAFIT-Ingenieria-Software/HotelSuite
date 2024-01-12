from django.urls import path
from .views import index, RoomManager

urlpatterns = [
    path('', index, name='admin_index'),

    path('rooms/', RoomManager.index, name='room_manager_index'),
    path('rooms/create/', RoomManager.create, name='room_manager_create'),
]
