from django.urls import path
from .views import *

urlpatterns = [
    path('notification',NotificationListView.as_view(),name='notification'),
    path('notification/<int:pk>',NotificationDetailView.as_view(),name='view_notification'),
    path('nextevent',NextEventListView.as_view(),name='nextevent'),
    path('nextevent/<int:pk>',NextEventDetailView.as_view(),name='view_nextevent'),

    path('api/register_user', UserRegistrationView.as_view(), name='user-registration'),
    path('api/login', UserLoginView.as_view(), name='user-login'),
    path('api/logout_user', UserLogoutView.as_view(), name='user-logout'),
    path('api/get_user',GetUserView.as_view(),name = 'get_user'),

    
]