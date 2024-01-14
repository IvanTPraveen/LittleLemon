from django.shortcuts import render
from rest_framework.decorators import api_view
from . import models
from .serializers import MenuItemSerializer
from rest_framework import generics

# Create your views here. 
class MenuItemsView(generics.ListCreateAPIView):
    queryset = models.Menu.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = models.Menu.objects.all()
    serializer_class = MenuItemSerializer

def index(request):
    return render(request, 'index.html', {})