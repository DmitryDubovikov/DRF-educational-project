import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Footballer


class FootballerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footballer
        fields = ('__all__')
