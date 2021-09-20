from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory
from .RoomForm import RoomForm

from django.views.generic import ListView, TemplateView, DetailView
from  django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
from meetings.models import Meeting, Room


class Detail(DetailView):
    model = Meeting
    template_name = 'meetings/detail.html'
    context_object_name = 'meeting_detail'


class MeetingCreate(CreateView):
    model = Meeting
    template_name = 'meetings/create_meeting.html'
    fields = '__all__'


class EditMeeting(UpdateView):
    model = Meeting
    template_name = 'meetings/edit_meeting.html'
    fields = ['title', 'date', 'start_time', 'duration', 'room']


class RoomList(ListView):
    model = Room
    template_name = 'meetings/roomList.html'
    context_object_name = 'room_list'


class RoomCreate(CreateView):
    model = Room
    template_name = 'meetings/create_room.html'
    fields = '__all__'


class EditRoom(UpdateView):
    model = Room
    template_name = 'meetings/edit_room.html'
    fields = '__all__'


class DeleteRoom(DeleteView):
    model = Room
    template_name = 'meetings/delete_room.html'
    success_url = reverse_lazy('room_list')