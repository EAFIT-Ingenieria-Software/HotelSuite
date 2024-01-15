from django.db import models
from UserManagement.models import User

# Create your models here.


def image_path(instance, filename):
    return f'rooms/{instance.id}/{filename}'


class Room(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.IntegerField()
    type = models.CharField(max_length=50)
    price = models.IntegerField()
    capacity = models.IntegerField()
    image = models.ImageField(upload_to=image_path)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "rooms"

    def __str__(self):
        return self.type

    def get_id(self):
        return self.id

    def get_number(self):
        return self.number

    def set_number(self, number):
        self.number = number

    def get_type(self):
        return self.type

    def set_type(self, type):
        self.type = type

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_capacity(self):
        return self.capacity

    def set_capacity(self, capacity):
        self.capacity = capacity

    def get_image(self):
        return self.image

    def set_image(self, image):
        self.image = image

    def get_created_at(self):
        return self.created_at

    def get_updated_at(self):
        return self.updated_at


class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.IntegerField()
    status = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "bookings"

    def __str__(self):
        return self.user

    def get_id(self):
        return self.id

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

    def get_user(self):
        return self.user

    def set_user(self, user):
        self.user = user

    def get_created_at(self):
        return self.created_at

    def get_updated_at(self):
        return self.updated_at


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.IntegerField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    entrance = models.DateTimeField()
    exit = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "items"

    def __str__(self):
        return self.name

    def get_id(self):
        return self.id

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_room(self):
        return self.room

    def set_room(self, room):
        self.room = room

    def get_booking(self):
        return self.booking

    def set_booking(self, booking):
        self.booking = booking

    def get_entrance(self):
        return self.entrance

    def set_entrance(self, entrance):
        self.entrance = entrance

    def get_exit(self):
        return self.exit

    def set_exit(self, exit):
        self.exit = exit

    def get_created_at(self):
        return self.created_at

    def get_updated_at(self):
        return self.updated_at
