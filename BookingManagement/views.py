from django.shortcuts import render

from .models import Room

# Create your views here.


class RoomView:
    def index(request):
        template_data = {}
        template_data['title'] = 'HotelSuite'
        template_data['section_title'] = 'Rooms'
        template_data['rooms'] = Room.objects.all()
        return render(request, 'rooms/index.html', {"template_data": template_data})
