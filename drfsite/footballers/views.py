from django.forms import model_to_dict
from rest_framework import generics, viewsets, mixins
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import Footballer, Category
from .serializers import FootballerSerializer


class FootballerViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.ListModelMixin,
                        GenericViewSet):
    queryset = Footballer.objects.all()
    serializer_class = FootballerSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Footballer.objects.all()[:3]
        else:
            return Footballer.objects.filter(pk=pk)


    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})
