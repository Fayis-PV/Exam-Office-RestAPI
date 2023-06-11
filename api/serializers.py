from rest_framework import serializers
from .models import NextEvents,Notification

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class NextEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NextEvents
        fields = '__all__'