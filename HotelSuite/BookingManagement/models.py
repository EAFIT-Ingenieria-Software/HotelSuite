from django.db import models

# Create your models here.


class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    entrance = models.TextField()
    departure = models.TextField()
    price = models.IntegerField()
    creationDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}'

    def get_id(self):
        return self.id

    def get_entrance(self):
        return self.entrance

    def set_entrance(self, entrance: str):
        self.entrance = entrance

    def get_departure(self):
        return self.departure

    def set_departure(self, departure: str):
        self.departure = departure

    def get_price(self):
        return self.price

    def set_price(self, price: int):
        self.price = price

    def get_creation_date(self):
        return self.creationDate

    def get_update_date(self):
        return self.updateDate


class Room(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.IntegerField()
    type = models.TextField()
    availability = models.BooleanField()
    price = models.IntegerField()
    capacity = models.IntegerField()
    creationDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.number}'

    def get_id(self):
        return self.id

    def get_number(self):
        return self.number

    def set_number(self, number: int):
        self.number = number

    def get_type(self):
        return self.type

    def set_type(self, type: str):
        self.type = type

    def get_availability(self):
        return self.availability

    def set_availability(self, availability: bool):
        self.availability = availability

    def get_price(self):
        return self.price

    def set_price(self, price: int):
        self.price = price

    def get_capacity(self):
        return self.capacity
    
    def set_capacity(self, capacity: int):
        self.capacity = capacity

    def get_creation_date(self):
        return self.creationDate

    def get_update_date(self):
        return self.updateDate


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.IntegerField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    creationDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}'

    def get_id(self):
        return self.id

    def get_price(self):
        return self.price

    def set_price(self, price: int):
        self.price = price

    def get_room(self):
        return self.room

    def set_room(self, room: Room):
        self.room = room

    def get_creation_date(self):
        return self.creationDate

    def get_update_date(self):
        return self.updateDate
