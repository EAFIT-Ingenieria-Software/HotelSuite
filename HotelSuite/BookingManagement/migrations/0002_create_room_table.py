# Generated by Django 4.2.6 on 2023-10-23 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BookingManagement', '0001_create_booking_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.IntegerField()),
                ('type', models.TextField()),
                ('availability', models.BooleanField()),
                ('price', models.IntegerField()),
                ('creationDate', models.DateTimeField(auto_now_add=True)),
                ('updateDate', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
