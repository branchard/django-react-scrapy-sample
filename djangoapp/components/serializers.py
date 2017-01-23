from rest_framework import serializers
from djangoapp.components.models import Component, Brand, Processor, Case, Motherboard, Socket, PowerSupplyFormFactor, Ram, RamFrequency, RamType, PciType, MotherBoardFormFactor
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


    class Meta:
        model = RamType
        fields = ('id', 'typeName')


class RamFrequencySerializer(serializers.ModelSerializer):


    class Meta:
        model = RamFrequency
        fields = ('id', 'frequency')


class PciTypeSerializer(serializers.ModelSerializer):


    class Meta:
        model = PciType
        fields = ('id', 'name')

class MotherBoardFormFactorSerializer(serializers.ModelSerializer):

    class Meta:
        model = MotherBoardFormFactor
        fields = ('id', 'name')


class MotherboardSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(many=False, read_only=True)
    socket = SocketSerializer(many=False, read_only=True)
    sale_set = SaleSerializer(many=True, read_only=True)

    ramtype = RamTypeSerializer(many=False, read_only=True)
    ramfrequency = RamFrequencySerializer(many=True, read_only=True)
    pcitypes = PciTypeSerializer(many=True, read_only=True)
    formfactor = MotherBoardFormFactorSerializer(many=False, read_only=True)


    class Meta:
        model = Motherboard
        fields = ('name', 'photoUrl', 'brand', 'ramSlots', 'maxRam', 'ramtype', 'ramfrequency', 'socket', 'pcitypes', 'formfactor', 'sale_set')


class RamSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(many=False, read_only=True)
    sale_set = SaleSerializer(many=True, read_only=True)

    ramtype = RamTypeSerializer(many=False, read_only=True)
    frequency = RamFrequencySerializer(many=False, read_only=True)


    class Meta:
        model = Ram
        fields = ('name', 'photoUrl', 'brand', 'capacity', 'quantity', 'ramtype', 'frequency', 'sale_set')


class PowerSupplyFormFactorSerializer(serializers.ModelSerializer):

    class Meta:
        model = PowerSupplyFormFactor
        fields = ('id', 'name')

class CaseSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(many=False, read_only=True)
    sale_set = SaleSerializer(many=True, read_only=True)

    powerSupplyFormFactor = PowerSupplyFormFactorSerializer(many=False, read_only=True)

    class Meta:
        model = Case
        fields = ('name', 'photoUrl', 'brand', 'weight', 'width', 'height', 'depth', 'powerSupplyFormFactor', 'sale_set')
