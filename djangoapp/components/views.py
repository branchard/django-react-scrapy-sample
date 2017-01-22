from rest_framework import viewsets
from djangoapp.components.serializers import ComponentsSerializer, ProcessorSerializer, MotherboardSerializer
from djangoapp.components.models import Component, Brand, Processor, Motherboard, Socket


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
