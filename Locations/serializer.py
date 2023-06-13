from rest_framework import serializers
from .models import Beautiful


class BeautifulSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beautiful
        fields = '__all__'

