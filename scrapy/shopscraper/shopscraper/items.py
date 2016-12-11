# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy_djangoitem import DjangoItem
from djangoapp.components.models import Component


class ShopscraperItem(DjangoItem):
    django_model = Component
