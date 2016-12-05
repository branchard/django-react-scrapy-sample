from rest_framework import serializers
from djangoapp.components.models import Component, Brand, Processor, Motherboard, Socket


class ComponentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Processor
        fields = ('name', 'brand')
