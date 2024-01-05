from django.shortcuts import render
from BookingManagement.models import Room

# Create your views here.


def index(request):
    template_data = {}
    template_data['title'] = 'HotelSuite'
    template_data['section_title'] = 'Home'

    return render(request, 'index.html', {"template_data": template_data})


class RoomManager:
    def index(request):
        template_data = {}
        template_data['title'] = 'HotelSuite'
        template_data['section_title'] = 'Rooms'

        template_data['rooms'] = Room.objects.all()

        return render(request, 'rooms/index.html', {"template_data": template_data})
