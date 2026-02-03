from .models import *
from rest_framework import serializers

class ShangpinguanliSer(serializers.ModelSerializer):
    class Meta:
        model = Shangpinguanli
        fields = '__all__'