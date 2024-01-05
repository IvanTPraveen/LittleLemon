from django.urls import path
from . import views

#url paths under this sentence

urlpatterns = [
    path('', views.index, name='index')
]