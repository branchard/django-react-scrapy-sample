from rest_framework import viewsets
from djangoapp.shops.serializers import ShopsSerializer, SaleSerializer
from djangoapp.shops.models import Shop, Sale


class ShopsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Shop.objects.all()
    serializer_class = ShopsSerializer

class SaleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
