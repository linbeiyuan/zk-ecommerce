from .models import *
from rest_framework import serializers

class DiscussshangpinguanliSer(serializers.ModelSerializer):
    class Meta:
        model = Discussshangpinguanli
        fields = '__all__'