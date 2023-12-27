from django.db import models

# Create your models here.
class Room(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.IntegerField()
    type = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField(upload_to="HotelSuite/room_images")
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

    def get_image(self):
        return self.image

    def set_image(self, image):
        self.image = image

    def get_created_at(self):
        return self.created_at

    def get_updated_at(self):
        return self.updated_at

class Date(models.Model):
    id = models.AutoField(primary_key=True)
    entrance = models.DateTimeField()
    departure = models.DateTimeField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "dates"

    def __str__(self):
        return self.date

    def get_id(self):
        return self.id

    def get_entrance(self):
        return self.entrance

    def set_entrance(self, entrance):
        self.entrance = entrance

    def get_departure(self):
        return self.departure

    def set_departure(self, departure):
        self.departure = departure

    def get_room(self):
        return self.room

    def set_room(self, room):
        self.room = room

    def get_created_at(self):
        return self.created_at

    def get_updated_at(self):
        return self.updated_at
