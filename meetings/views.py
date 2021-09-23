from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory
from .RoomForm import RoomForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
from meetings.models import Meeting, Room


class Detail(DetailView):
    model = Meeting
    template_name = 'meetings/detail.html'
    context_object_name = 'meeting_detail'


class MeetingCreate(LoginRequiredMixin, CreateView):
    model = Meeting
    template_name = 'meetings/create_meeting.html'
    fields = ['title', 'date', 'start_time', 'duration', 'room']
    login_url = 'login'

    def form_valid(self, form):
        form.instance.organizer = self.request.user
        return super().form_valid(form)


class EditMeeting(LoginRequiredMixin, UpdateView):
    model = Meeting
    template_name = 'meetings/edit_meeting.html'
    fields = ['title', 'date', 'start_time', 'duration', 'room']
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.organizer != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class DeleteMeeting(LoginRequiredMixin, DeleteView):
    model = Meeting
    template_name = 'meetings/delete_meeting.html'
    success_url = reverse_lazy('welcome')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.organizer != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class RoomList(LoginRequiredMixin, ListView):
    model = Room
    template_name = 'meetings/roomList.html'
    context_object_name = 'room_list'
    login_url = 'login'


class RoomCreate(LoginRequiredMixin, CreateView):
    model = Room
    template_name = 'meetings/create_room.html'
    fields = '__all__'
    login_url = 'login'


class EditRoom(LoginRequiredMixin, UpdateView):
    model = Room
    template_name = 'meetings/edit_room.html'
    fields = '__all__'
    login_url = 'login'


class DeleteRoom(LoginRequiredMixin, DeleteView):
    model = Room
    template_name = 'meetings/delete_room.html'
    success_url = reverse_lazy('room_list')
    login_url = 'login'