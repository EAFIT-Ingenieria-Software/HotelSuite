from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse

from BookingManagement.models import Room
from .forms import RoomCreationForm

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

    def create(request):
        template_data = {}
        template_data['title'] = 'HotelSuite'
        template_data['section_title'] = 'Room creation'

        if request.method == 'POST':
            room = Room()
            room.set_number(request.POST['number'])
            room.set_type(request.POST['type'])
            room.set_price(request.POST['price'])
            room.set_capacity(request.POST['capacity'])
            room.save()

            room.set_image(request.FILES['image'])
            room.save()

            messages.success(request, 'Room created successfully')

            return redirect(reverse('room_manager_index'))

        elif request.method == 'GET':
            form = RoomCreationForm(request.POST, request.FILES)

            return render(request, 'rooms/create.html', {"template_data": template_data, "form": form})

        return render(request, 'rooms/create.html', {"template_data": template_data})
