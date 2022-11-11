import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Footballer


# class FootballerModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


class FootballerSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()


# def encode():
#     model = FootballerModel('Denilson', 'Denilson de Oliveira Araujo')
#     model_sr = FootballerSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
# def decode():
#     stream = io.BytesIO(b'{"title":"Denilson","content":"Denilson de Oliveira Araujo"}')
#     data = JSONParser().parse(stream)
#     serializer = FootballerSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
