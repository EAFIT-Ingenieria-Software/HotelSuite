from django.shortcuts import render
from . import models as models

# Create your views here.


class Booking:
    def index(request):
        templateData = {
            'title': 'Booking',
        }
        return render(request, 'booking/index.html', {"templateData": templateData})


class Room:
    def index(request):
        rooms = models.Room.objects.all()
        templateData = {
            'title': 'Room',
            'rooms': rooms,
        }
        return render(request, 'room/index.html', {"templateData": templateData})

    def show(request, room_id):
        room = models.Room.objects.get(pk=room_id)
        templateData = {
            'title': 'Room',
            'room': room,
        }
        return render(request, 'room/show.html', {"templateData": templateData})
