from django.forms import model_to_dict
from rest_framework import generics, viewsets, mixins
from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import Footballer, Category
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import FootballerSerializer


class FootballerAPIList(generics.ListCreateAPIView):
    queryset = Footballer.objects.all()
    serializer_class = FootballerSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class FootballerAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Footballer.objects.all()
    serializer_class = FootballerSerializer
    permission_classes = (IsAuthenticated, )
    # authentication_classes = (TokenAuthentication, )


class FootballerAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Footballer.objects.all()
    serializer_class = FootballerSerializer
    permission_classes = (IsAdminOrReadOnly, )
