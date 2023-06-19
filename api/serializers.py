from rest_framework import serializers
from .models import NextEvents,Notification
from django.contrib.auth.models import User

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class NextEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NextEvents
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username','email', 'password','is_staff')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        if validated_data['is_staff'] == True:
            user = User.objects.create_user(**validated_data)
            user.set_password(password)
            user.is_staff = True
            print(user ,'is a staff')
            user.save()
            return user
        user = User(**validated_data)
        user.set_password(password)
        print(user,'created')
        user.save()
        return user

        