from rest_framework import serializers
from djangoapp.components.models import Component, Brand, Processor, Motherboard, Socket
from djangoapp.shops.serializers import SaleSerializer


class ComponentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = ('name', 'brand')

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'name')

class SocketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Socket
        fields = ('id', 'name')

class ProcessorSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(many=False, read_only=True)
    socket = SocketSerializer(many=False, read_only=True)
    sale_set = SaleSerializer(many=True, read_only=True)

    class Meta:
        model = Processor
        fields = ('name', 'photoUrl', 'brand', 'frequency', 'cores', 'socket', 'sale_set')

class RamTypeSerializer(serializers.ModelSerializer):
    pass


class MotherboardSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(many=False, read_only=True)
    socket = SocketSerializer(many=False, read_only=True)
    sale_set = SaleSerializer(many=True, read_only=True)

    class Meta:
        model = Processor
        fields = ('name', 'photoUrl', 'brand', 'ramSlots', 'maxRam', 'ramtype', 'ramfrequency', 'socket', 'pcitypes', 'formfactor', 'sale_set')
