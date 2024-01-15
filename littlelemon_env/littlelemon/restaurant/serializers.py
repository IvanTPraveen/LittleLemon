#define Serializer class for User model
from django.contrib.auth.models import User
from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Menu
        fields = "__all__"

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Booking
        fields = "__all__"