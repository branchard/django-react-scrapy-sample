from django.db import models
from djangoapp.components.models import Component


class Shop(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()


class Sale(models.Model):
    price = models.DecimalField(max_digits=6, decimal_places=2)  # in euro
    deliveryPrice = models.DecimalField(max_digits=6, decimal_places=2, null=True)  # in euro
    stockQuantity = models.IntegerField(null=True)  # approximatif car la boutique n'est pas mise à jour en temps reel
    note = models.IntegerField(null=True)  # number of stars
    shop = models.ForeignKey(
        'Shop',
        on_delete=models.CASCADE,
    )
    component = models.ForeignKey(
        Component,
        on_delete=models.CASCADE,
    )


class ItemToScrap(models.Model):
    url = models.URLField() # l'url de l'objet à scraper
    itemId = models.BigIntegerField(
        null=True,
        blank=True
    )  # id de l'item, permet de savoir quelles items sont identiques. C'est à l'administrateur lui même de s'organiser pour faire en sorte que les même objets est le même id
    toScrap = models.BooleanField(default=False)  # Permet de dire à scrapy de ne pas scraper l'objet
    sale = models.OneToOneField(
        'Sale',
        on_delete=models.SET_NULL,
        null=True
    )
