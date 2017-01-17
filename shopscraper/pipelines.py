# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from djangoapp.components.models import Component, Brand

class ShopscraperPipeline(object):
    def process_item(self, item, spider):
        brand = Brand.objects.filter(name__iexact = item['brand'])  # __iexact -> Case-insensitive exact match
        if(brand.count() <= 0): #  brand dont exists -> create new brand
            # brand = Brand(name=item['brand'])
            brand = Brand.objects.create(name=item['brand'])
        else:
            brand = brand[0]
        item['brand']=brand
        item.save()
        return item
