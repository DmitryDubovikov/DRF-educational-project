from django.forms import model_to_dict
from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Footballer
from .serializers import FootballerSerializer

class FootballerAPIView(APIView):
    def get(self, request):
        lst = Footballer.objects.all().values()
        return Response({'articles': list(lst)})

    def post(self, request):
        new_article = Footballer.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )
        return Response({'new_article': model_to_dict(new_article)})



# Create your views here.
# class FootballerAPIView(generics.ListAPIView):
#     queryset = Footballer.objects.all()
#     serializer_class = FootballerSerializer
