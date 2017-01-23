from rest_framework import viewsets
from djangoapp.components.serializers import ComponentsSerializer, ProcessorSerializer, CaseSerializer, MotherboardSerializer, RamSerializer, GraphicCardSerializer, HardDriveSerializer, PowerSupplySerializer
from djangoapp.components.models import Component, Brand, Processor, Motherboard, Socket, Ram, Case, GraphicCard, HardDrive, PowerSupply


class ComponentsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Component.objects.all()
    serializer_class = ComponentsSerializer

class ProcessorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Processor.objects.all()
    serializer_class = ProcessorSerializer

class MotherboardViewSet(viewsets.ModelViewSet):
    queryset = Motherboard.objects.all()
    serializer_class = MotherboardSerializer

class RamViewSet(viewsets.ModelViewSet):
    queryset = Ram.objects.all()
    serializer_class = RamSerializer

class CaseViewSet(viewsets.ModelViewSet):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer

class GraphicCardViewSet(viewsets.ModelViewSet):
    queryset = GraphicCard.objects.all()
    serializer_class = GraphicCardSerializer

class HardDriveViewSet(viewsets.ModelViewSet):
    queryset = HardDrive.objects.all()
    serializer_class = HardDriveSerializer

class PowerSupplyViewSet(viewsets.ModelViewSet):
    queryset = PowerSupply.objects.all()
    serializer_class = PowerSupplySerializer
