from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from backend.models import *
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from django.http import Http404


# Create your views here.
def index(request):
    return HttpResponse("<p>It worked</p>")

class UsersViewSet(viewsets.ModelViewSet):
    """ API endpoint to perform CRUD operation as well as list all the users"""
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class UserDetailViewSet(APIView):
    def get_user(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404("User does not exist")
    
    def get(self, request, pk, format=None):
        user = self.get_user(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)