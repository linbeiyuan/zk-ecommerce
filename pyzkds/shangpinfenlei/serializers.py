from .models import *
from rest_framework import serializers

class ShangpinfenleiSer(serializers.ModelSerializer):
    class Meta:
        model = Shangpinfenlei
        fields = '__all__'