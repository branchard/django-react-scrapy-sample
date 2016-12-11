from rest_framework import serializers
from djangoapp.shops.models import Shop


class ShopsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('name', 'url')
