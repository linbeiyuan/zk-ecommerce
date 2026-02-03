from .models import *
from rest_framework import serializers

class CrkSer(serializers.ModelSerializer):
    class Meta:
        model = Crk
        fields = '__all__'