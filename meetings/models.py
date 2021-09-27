from django.db import models
from django.contrib.auth import get_user_model
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
    organizer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} at {self.start_time} on {self.date} on {self.room} organized by {self.organizer}"

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])

    def save(self, *args, **kwargs):
        if self.date < datetime.date.today():
            raise ValidationError("The date cannot be in the past!")
        super(Meeting, self).save(*args, **kwargs)


class Comment(models.Model):
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=150)
    commenter = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('welcome')