from django.shortcuts import render
from rest_framework import viewsets
from .serializers import movie_serializer
from .models import movie_data
# Create your views here.

class movie_view(viewsets.ModelViewSet):
    queryset=movie_data.objects.all()
    serializer_class=movie_serializer

class action_m(viewsets.ModelViewSet):
    queryset=movie_data.objects.filter(typ='action')
    serializer_class=movie_serializer

class comedy_m(viewsets.ModelViewSet):
    queryset=movie_data.objects.filter(typ='comedy')
    serializer_class=movie_serializer
