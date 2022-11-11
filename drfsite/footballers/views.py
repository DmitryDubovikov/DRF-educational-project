from rest_framework import generics
from django.shortcuts import render
from .models import Footballer
from .serializers import FootballerSerializer


# Create your views here.
class FootballerAPIView(generics.ListAPIView):
    queryset = Footballer.objects.all()
    serializer_class = FootballerSerializer