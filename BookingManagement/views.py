from django.shortcuts import render

from .forms import RoomAvailabilityForm
from .models import Item, Room

# Create your views here.


class RoomView:
    def index(request):
        template_data = {}
        template_data['title'] = 'HotelSuite'
        template_data['section_title'] = 'Rooms'
        form = RoomAvailabilityForm(request.POST)
        if request.method == 'POST':
            if form.is_valid():
                entrance_date = form.cleaned_data['entrance_date']
                exit_date = form.cleaned_data['exit_date']
                rooms_ids = Item.objects.filter(
                    entrance_date__gte=entrance_date,
                    exit_date__lte=exit_date
                ).values_lst('room_id', flat=True).distinct()
                rooms = Room.objects.exclude(id__in=rooms_ids)
                template_data['rooms'] = rooms
        else:
            template_data['form'] = RoomAvailabilityForm()
            template_data['rooms'] = Room.objects.all()
        return render(request, 'rooms/index.html', {"template_data": template_data, "form": form})
