from rest_framework import generics
from .models import NextEvents,Notification
from .serializers import NextEventsSerializer,NotificationSerializer
from rest_framework import permissions
#NotificationListView, NotificationDetailView, NextEventListView, NextEventDetailView

class NotificationListView(generics.ListCreateAPIView):
    serializer_class = NotificationSerializer

    def get_queryset(self):
        queryset = Notification.objects.all()
        return queryset
    
class NotificationDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()
    # permission_classes = [permissions.IsAuthenticated]

class NextEventListView(generics.ListCreateAPIView):
    serializer_class = NextEventsSerializer
    queryset = NextEvents.objects.all()

class NextEventDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NextEventsSerializer
    queryset = NextEvents.objects.all()