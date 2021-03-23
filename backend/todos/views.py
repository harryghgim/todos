# from django.shortcuts import render

from .models import *
from .serializers import *

from rest_framework import generics

# Create your views here.

class TaskList(generics.ListCreateAPIView):
    """
    Perform Task list or create an instance 
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    perform RUD of an instance
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
