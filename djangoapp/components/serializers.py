from rest_framework import serializers
from djangoapp.components.models import Component, Brand, Processor, Motherboard, Socket


class ComponentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = ('name', 'brand')

class SocketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Socket
        fields = ('id', 'name')

class ProcessorSerializer(serializers.ModelSerializer):
    socket = SocketSerializer(many=False, read_only=True)

    class Meta:
        model = Processor
        fields = ('name', 'brand', 'frequency', 'cores', 'socket')
