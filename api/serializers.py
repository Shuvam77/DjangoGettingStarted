from django.contrib.auth import get_user_model
from rest_framework import serializers

from meetings.models import Meeting


class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = ('id', 'title', 'date', 'start_time', 'duration', 'organizer', 'room', 'comments')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'age', 'email')