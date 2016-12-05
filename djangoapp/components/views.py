from rest_framework import viewsets
from djangoapp.components.serializers import ComponentsSerializer
from djangoapp.components.models import Component, Brand, Processor, Motherboard, Socket


class ComponentsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Processor.objects.all()
    serializer_class = ComponentsSerializer
