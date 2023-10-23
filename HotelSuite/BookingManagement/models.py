from django.db import models

# Create your models here.


class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    entrance = models.TextField()
    departure = models.TextField()
    price = models.IntegerField()
    creationDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

    def getId(self) -> int:
        return self.id

    def getEntrance(self) -> str:
        return self.entrance

    def setEntrance(self, entrance: str):
        self.entrance = entrance

    def getDeparture(self) -> str:
        return self.departure

    def setDeparture(self, departure: str):
        self.departure = departure

    def getPrice(self) -> int:
        return self.price

    def setPrice(self, price: int):
        self.price = price

    def getCreationDate(self) -> str:
        return self.creationDate

    def getUpdateDate(self) -> str:
        return self.updateDate


class Room(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.IntegerField()
    type = models.TextField()
    availability = models.BooleanField()
    price = models.IntegerField()
    creationDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

    def getId(self) -> int:
        return self.id

    def getNumber(self) -> int:
        return self.number

    def setNumber(self, number: int):
        self.number = number

    def getType(self) -> str:
        return self.type

    def setType(self, type: str):
        self.type = type

    def getAvailability(self) -> bool:
        return self.availability

    def setAvailability(self, availability: bool):
        self.availability = availability

    def getPrice(self) -> int:
        return self.price

    def setPrice(self, price: int):
        self.price = price

    def getCreationDate(self) -> str:
        return self.creationDate

    def getUpdateDate(self) -> str:
        return self.updateDate
