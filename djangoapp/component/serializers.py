from rest_framework import serializers
from djangoapp.component.models import Component, Brand, Processor, Motherboard, Socket


class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Processor
        fields = ('name', 'brand')
