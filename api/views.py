from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import generics, permissions, viewsets

from meetings.models import Meeting
from .permissions import IsOrganizerOrReadOnly
from .serializers import MeetingSerializer, UserSerializer


# Create your views here.

class MeetingViewSet(viewsets.ModelViewSet):
    permission_classes = (IsOrganizerOrReadOnly,)
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

