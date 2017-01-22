# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from djangoapp.components.models import Component, Processor, Brand, Socket
from djangoapp.shops.models import Sale, Shop

class ShopscraperPipeline(object):
    def process_item(self, item, spider):
        sale = Sale(price=item["price"], shop=Shop.objects.filter(name__iexact = item['shopName'])[0])

        if(item['itemType'] == "processor"):
            print("Processor --")
            component = Processor()

            component.frequency = item["frequency"]
            component.cores = item["cores"]

            socket = Socket.objects.filter(name__iexact = item['socket'])  # __iexact -> Case-insensitive exact match
            if(socket.count() <= 0): # if socket dont exists
                socket = Socket.objects.create(name=item['socket'])
            else:
                socket = socket[0]
            component.socket = socket


        component.name = item["name"]
        component.photoUrl = item["photo"]

        brand = Brand.objects.filter(name__iexact = item['brand'])  # __iexact -> Case-insensitive exact match
        if(brand.count() <= 0): #  brand dont exists -> create new brand
            # brand = Brand(name=item['brand'])
            brand = Brand.objects.create(name=item['brand'])
        else:
            brand = brand[0]

        component.brand = brand

        component.save()

        sale.component = component

        sale.save()

        item['itemDjangoModel'].sale = sale
        item['itemDjangoModel'].save()

        return sale
