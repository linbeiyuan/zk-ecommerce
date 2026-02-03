from .models import *
from rest_framework import serializers

class ShangjiaSer(serializers.ModelSerializer):
    class Meta:
        model = Shangjia
        fields = '__all__'