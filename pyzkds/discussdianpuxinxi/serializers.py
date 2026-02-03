from .models import *
from rest_framework import serializers

class DiscussdianpuxinxiSer(serializers.ModelSerializer):
    class Meta:
        model = Discussdianpuxinxi
        fields = '__all__'