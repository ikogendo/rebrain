from rest_framework import serializers
from .models import station


class stationSerializer(serializers.ModelSerializer):
    class Meta:
        model = station
        fields = ('name','user','ip_address','place_id')