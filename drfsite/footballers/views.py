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
        serializer.save()
        return Response({'new_article': serializer.data})

    def put(self, request, *args, **kwars):
        pk = kwars.get('pk', None)
        if not pk:
            return Response({'error', 'Method PUT is not allowed (without pk)!'})

        try:
            instance = Footballer.objects.get(pk=pk)
        except:
            return Response({'error', f'Object with pk={pk} does not exist!'})

        serializer = FootballerSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'article': serializer.data})

    def delete(self, request, *args, **kwars):
        pk = kwars.get('pk', None)
        if not pk:
            return Response({'error', 'Method DELETE is not allowed (without pk)!'})

        try:
            instance = Footballer.objects.get(pk=pk)
        except:
            return Response({'error', f'Object with pk={pk} does not exist!'})

        instance.delete()
        return Response({'article deleted': f'article with pk={pk} deleted'})



# Create your views here.
# class FootballerAPIView(generics.ListAPIView):
#     queryset = Footballer.objects.all()
#     serializer_class = FootballerSerializer
