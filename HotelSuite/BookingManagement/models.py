from django.db import models

# Create your models here.


class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    entarance = models.CharField(max_length=100)
    departure = models.CharField(max_length=100)
    creationDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)
    price = models.IntegerField()
    # userId = models.ForeignKey('User', on_delete=models.CASCADE)
    # itemId = models.ForeignKey('Item', on_delete=models.CASCADE)

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'booking'
        ordering = ['id', 'entarance', 'departure', 'creationDate',
                    'updateDate', 'price']
