from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from djangoapp.components.models import Component


class Shop(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()


class Sale(models.Model):
    url = models.URLField()
    price = models.DecimalField(max_digits=6, decimal_places=2)  # in euro
    deliveryPrice = models.DecimalField(max_digits=6, decimal_places=2)  # in euro
    stockQuantity = models.IntegerField()  # approximatif car la boutique n'est pas mise à jour en temps reel
    note = models.IntegerField()  # number of stars
    shop = models.ForeignKey(
        'Shop',
        on_delete=models.CASCADE,
    )
    component = models.ForeignKey(
        Component,
        on_delete=models.CASCADE,
    )

class ItemToScrap(models.Model):
    url = models.URLField()
    itemId = models.BigIntegerField() # id de l'item, permet de savoir quelles items sont identiques
    sale = models.OneToOneField(
        'Sale',
        on_delete=models.SET_NULL,
        null=True
    )
