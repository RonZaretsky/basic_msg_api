from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
# Create your views here.

class Messages(generics.ListCreateAPIView):
    queryset = MessageInfoItem.objects.all()
    serializer_class = MessageInfoItemSerializer