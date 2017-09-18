from django.shortcuts import render
from .models import *
from rest_framework import generics
from django.contrib.auth.models import User
from api.serializers import *
from rest_framework import filters

# Create your views here.

class user_search(generics.ListAPIView):
    serializer_class = userSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields =['id', 'last_login', 'is_superuser','username','first_name','last_name','email','date_joined',]
    queryset = User.objects.all()

class add_user(generics.CreateAPIView):
    serializer_class = add_user_Serializer
    queryset=User.objects.all()
