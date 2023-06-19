from rest_framework import generics
from .models import NextEvents,Notification
from .serializers import NextEventsSerializer,NotificationSerializer,UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import login,logout,authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User,AnonymousUser
from .permissions import IsAdminOrReadOnly,IsSuperUserOrReadOnly


class NotificationListView(generics.ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAdminOrReadOnly]

class NotificationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAdminOrReadOnly]

class NextEventListView(generics.ListCreateAPIView):
    queryset = NextEvents.objects.all()
    serializer_class = NextEventsSerializer
    permission_classes = [IsAdminOrReadOnly]

class NextEventDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NextEvents.objects.all()
    serializer_class = NextEventsSerializer
    permission_classes = [IsAdminOrReadOnly]


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsSuperUserOrReadOnly]


class UserLoginView(APIView):
    def post(self, request):
        user = request.user
        if not user.is_authenticated:
            username = request.data.get('username')
            password = request.data.get('password')
            
            user = User.objects.filter(username=username).first()
            if user is None or not user.check_password(password):
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
            token, _ = Token.objects.get_or_create(user=user)
            authenticate(request)
            login(request,user=user)
            return Response({'user_info':{
                    'id':user.id,
                    'username':user.username,
                    'email':user.email,
                    'is_staff':user.is_staff,
                },
                'token': token.key})
        return Response('User is already authenticated',status=status.HTTP_400_BAD_REQUEST)

class UserLogoutView(APIView):

    def post(self, request):
        
        user = request.user
        if user.is_authenticated:
            logout(request)
            if user.auth_token:
                user.auth_token.delete()
            return Response(status=status.HTTP_200_OK)
        return Response('Please Login')


class GetUserView(APIView):
    permission_classes = [IsAdminOrReadOnly]
    
    def get(self,request):
        user = request.user
        if user.is_authenticated:
            return Response({
                'user_info':{
                    'id':user.id,
                    'username':user.username,
                    'email':user.email
                }
            })
        return Response({'error':'not authenticated'},status= status.HTTP_400_BAD_REQUEST) 
    
# @api_view()
# def make_token(request):
#     user = request.user
#     token, _ = Token.objects.get_or_create(user=user)
#     print(user, ':', token.key)
#     return Response({'token': token.key})

# from django.views import View
# from django.http import JsonResponse


# class GetCSRFTokenView(View):
#     def get(self, request):
#         print(request.COOKIES['csrftoken'])
#         return JsonResponse({'csrfToken': request.COOKIES['csrftoken']})
