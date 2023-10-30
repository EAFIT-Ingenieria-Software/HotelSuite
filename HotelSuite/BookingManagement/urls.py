from django.urls import path
import BookingManagement.views as views

class Booking:
    urlpatterns = [
        path('bookings/', views.Booking.index, name='booking.index')
    ]

class Room:
    urlpatterns = [
        path('', views.Room.index, name='room.index'),
        path('room/<int:id>', views.Room.show, name='room.show'),
    ]