from rest_framework import viewsets
from djangoapp.shops.serializers import ShopsSerializer
from djangoapp.shops.models import Shop


class ShopsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Shop.objects.all()
    serializer_class = ShopsSerializer
