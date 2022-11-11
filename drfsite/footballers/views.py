from django.forms import model_to_dict
from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Footballer
from .serializers import FootballerSerializer

class FootballerAPIView(APIView):
    def get(self, request):
        articles_queryset = Footballer.objects.all()
        return Response({'articles': FootballerSerializer(articles_queryset, many=True).data})

    def post(self, request):

        serializer = FootballerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        new_article = Footballer.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )
        return Response({'new_article': FootballerSerializer(new_article).data})



# Create your views here.
# class FootballerAPIView(generics.ListAPIView):
#     queryset = Footballer.objects.all()
#     serializer_class = FootballerSerializer
