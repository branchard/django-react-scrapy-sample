from rest_framework import viewsets
from djangoapp.component.serializers import ComponentSerializer
from djangoapp.component.models import Component, Brand, Processor, Motherboard, Socket


class ComponentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Processor.objects.all()
    serializer_class = ComponentSerializer
