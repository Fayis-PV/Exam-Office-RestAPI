from django.urls import path
from .views import NotificationListView, NotificationDetailView, NextEventListView, NextEventDetailView

urlpatterns = [
    path('notification',NotificationListView.as_view(),name='notification'),
    path('notification/<int:pk>',NotificationDetailView.as_view(),name='view_notification'),
    path('nextevent',NextEventListView.as_view(),name='nextevent'),
    path('nextevent/<int:pk>',NextEventDetailView.as_view(),name='view_nextevent'),
]
