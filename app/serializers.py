from rest_framework import serializers
from .models import NameModel


class NameSerializer (serializers.ModelSerializer) :
    class Meta :
        model = NameModel
        fields = '__all__'
