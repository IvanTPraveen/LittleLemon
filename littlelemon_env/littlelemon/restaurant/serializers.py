#define Serializer class for User model
from django.contrib.auth.models import User
from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
        
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Menu
        fields = ['Title', 'Price', 'inventory']