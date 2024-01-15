from django.urls import path
from .views import index, RoomManager

urlpatterns = [
    path('', index, name='admin_index'),

    path('rooms/', RoomManager.index, name='room_manager_index'),
    path('rooms/create/', RoomManager.create, name='room_manager_create'),
    path('rooms/view/<int:id>/', RoomManager.view, name='room_manager_view'),
    path('rooms/edit/<int:id>/', RoomManager.edit, name='room_manager_edit'),
    path('rooms/delete/<int:id>/', RoomManager.delete, name='room_manager_delete'),
]
