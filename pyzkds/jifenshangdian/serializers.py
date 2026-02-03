from .models import *
from rest_framework import serializers

class JifenshangdianSer(serializers.ModelSerializer):
    class Meta:
        model = Jifenshangdian
        fields = '__all__'