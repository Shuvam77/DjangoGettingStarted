from django.db import models
from datetime import time

import datetime
from django.core.exceptions import ValidationError
from django.urls import reverse

# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=50)
    floor_num = models.IntegerField()
    room_num = models.IntegerField()

    def __str__(self):
        return f"{self.name}: Room Number {self.room_num} on Floor {self.floor_num}"

    def get_absolute_url(self):
        return reverse('room_list')


class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)

    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} at {self.start_time} on {self.date} on {self.room}"

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])

    def save(self, *args, **kwargs):
        if self.date < datetime.date.today():
            raise ValidationError("The date cannot be in the past!")
        super(Meeting, self).save(*args, **kwargs)