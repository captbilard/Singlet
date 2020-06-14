from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from backend.models import *
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
# from rest_framework.views import APIView
# from rest_framework.response import Response
from .serializers import *
# from django.http import Http404


# Create your views here.
def index(request):
    return render(request, "singlet/index.html")

# class AdminUsersView(viewsets.ModelViewSet):
#     """ API endpoint to perform CRUD operation as well as list all the users"""
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAdminUser]

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

  

    