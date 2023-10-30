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

    def get_id(self) -> int:
        return self.id

    def get_entrance(self) -> str:
        return self.entrance

    def set_entrance(self, entrance: str):
        self.entrance = entrance

    def get_departure(self) -> str:
        return self.departure

    def set_departure(self, departure: str):
        self.departure = departure

    def get_price(self) -> int:
        return self.price

    def set_price(self, price: int):
        self.price = price

    def get_creation_date(self) -> str:
        return self.creationDate

    def get_update_date(self) -> str:
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

    def get_id(self) -> int:
        return self.id

    def get_number(self) -> int:
        return self.number

    def set_number(self, number: int):
        self.number = number

    def get_type(self) -> str:
        return self.type

    def set_type(self, type: str):
        self.type = type

    def get_availability(self) -> bool:
        return self.availability

    def set_availability(self, availability: bool):
        self.availability = availability

    def get_price(self) -> int:
        return self.price

    def set_price(self, price: int):
        self.price = price

    def get_creation_date(self) -> str:
        return self.creationDate

    def get_update_date(self) -> str:
        return self.updateDate


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.IntegerField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    creationDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}'

    def get_id(self) -> int:
        return self.id

    def get_price(self) -> int:
        return self.price

    def set_price(self, price: int):
        self.price = price

    def get_room(self) -> Room:
        return self.room

    def set_room(self, room: Room):
        self.room = room

    def get_creation_date(self) -> str:
        return self.creationDate

    def get_update_date(self) -> str:
        return self.updateDate
