from rest_framework import serializers
from djangoapp.shops.models import Shop, Sale


class ShopsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('name', 'url')

class SaleSerializer(serializers.ModelSerializer):
    shop = ShopsSerializer(many=False, read_only=True)

    class Meta:
        model = Sale
        fields = ('price', 'deliveryPrice', 'stockQuantity', 'note', 'shop')
