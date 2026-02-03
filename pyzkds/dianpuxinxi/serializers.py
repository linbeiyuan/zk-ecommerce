from .models import *
from rest_framework import serializers

class DianpuxinxiSer(serializers.ModelSerializer):
    class Meta:
        model = Dianpuxinxi
        fields = '__all__'