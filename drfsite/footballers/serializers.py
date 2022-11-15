from rest_framework import serializers
from .models import Footballer


class FootballerSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Footballer
        fields = ('__all__')
