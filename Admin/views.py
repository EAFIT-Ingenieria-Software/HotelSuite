from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse

from BookingManagement.models import Room
from .forms import RoomCreationForm, RoomEditForm

# Create your views here.


def index(request):
    template_data = {}
    template_data['title'] = 'HotelSuite'
    template_data['section_title'] = 'Home'
    return render(request, 'admin_index.html', {"template_data": template_data})


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

    def view(request, id):
        template_data = {}
        template_data['title'] = 'HotelSuite'
        template_data['section_title'] = 'Room'
        room = get_object_or_404(Room, pk=id)
        template_data['room'] = room
        return render(request, 'rooms/view.html', {"template_data": template_data})

    def edit(request, id):
        template_data = {}
        template_data['title'] = 'HotelSuite'
        template_data['section_title'] = 'Room edit'
        room = get_object_or_404(Room, pk=id)
        if request.method == 'GET':
            form = RoomEditForm(instance=room)
            return render(request, 'rooms/edit.html', {"template_data": template_data, "form": form})
        elif request.method == 'POST':
            form = RoomEditForm(request.POST, request.FILES, instance=room)
            if form.is_valid():
                form.save()
                messages.success(request, 'Room updated successfully')
                return redirect(reverse('room_manager_index'))
            return render(request, 'rooms/edit.html', {"template_data": template_data, "form": form})
        return render(request, 'rooms/edit.html', {"template_data": template_data})

    def delete(request, id):
        room = get_object_or_404(Room, pk=id)
        room.delete()
        messages.success(request, 'Room deleted successfully')
        return redirect(reverse('room_manager_index'))
