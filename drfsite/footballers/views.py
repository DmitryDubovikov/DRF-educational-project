from django.forms import model_to_dict
from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Footballer
from .serializers import FootballerSerializer


class FootballerAPIList(generics.ListCreateAPIView):
    queryset = Footballer.objects.all()
    serializer_class = FootballerSerializer

