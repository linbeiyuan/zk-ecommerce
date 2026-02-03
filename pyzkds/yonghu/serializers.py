from .models import *
from rest_framework import serializers

class YonghuSer(serializers.ModelSerializer):
    class Meta:
        model = Yonghu
        fields = '__all__'