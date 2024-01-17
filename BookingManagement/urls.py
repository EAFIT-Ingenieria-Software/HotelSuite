from django.urls import path, include

from . import views


class RoomUrls:
    urlpatterns = [
        path("", views.RoomView.index, name="rooms_index"),
    ]
