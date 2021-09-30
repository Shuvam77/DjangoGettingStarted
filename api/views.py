from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import generics, permissions

from meetings.models import Meeting
from .permissions import IsOrganizerOrReadOnly
from .serializers import MeetingSerializer, UserSerializer


# Create your views here.

class MeetingCreateView(generics.ListCreateAPIView):

    # View based permission
    # permission_classes = (permissions.IsAuthenticated,)

    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer


class MeetingDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOrganizerOrReadOnly,)
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer


class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

