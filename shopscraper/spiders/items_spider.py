from functools import wraps
from scrapy.spider import Spider
from scrapy.utils.python import get_func_args
import scrapy
from djangoapp.shops.models import ItemToScrap
from shopscraper.items import ShopscraperItem, ProcessorItem

def callback_args(f):
    args = get_func_args(f)[2:]
    @wraps(f)
    def wrapper(spider, response):
        return f(spider, response,
            **{k:response.meta[k] for k in args if k in response.meta})
    return wrapper

class ShopscraperSpider(scrapy.Spider):
    name = "shopscraper"
    allowed_domains = ["www.ldlc.com"]

    def start_requests(self):
        print("##### start_requests #####")
        itemsToScrap = ItemToScrap.objects.all()
        for item in itemsToScrap:
            if(item.toScrap and item.sale == None):
                yield scrapy.Request(url=item.url, callback=self.parse, meta={'itemDjangoModel': item})

    @callback_args
    def parse(self, response, itemDjangoModel):
        # define item type
        itemType = response.xpath("//ul[contains(@class, 'cheminDeFer')]//li[contains(@class, 'last')]//span//text()").extract()[0]
        if(itemType == "Processeur"):
            itemType = "processor"


        parsedItem = self.ldlcParse(response, itemType)
        parsedItem['itemType'] = itemType
        parsedItem['itemDjangoModel'] = itemDjangoModel

        return parsedItem #return item to the pipeline


    def ldlcParse(self, response, itemType):
        specsParent = response.xpath("//table[@id='productParametersList']")
        def getSpec(specName):
            return specsParent.xpath("//*[contains(text(),'{}')]/../..//td[2]//*[not(*)]//text()".format(specName))[0].extract()

        component = dict()

        component["price"] = float(response.xpath("//meta[@itemprop='price']/@content")[0].extract().replace(',', '.'))
        component["shopName"] = "ldlc"

        component["name"] = getSpec("Désignation")
        component["brand"] = getSpec("Marque")

        if(itemType == "processor"):
            component["frequency"] = float(getSpec("Fréquence CPU").replace("GHz", "").replace(" ", "").replace(",", "."))
            component["cores"] = int(getSpec("Nombre de core"))
            component["socket"] = getSpec("Support du processeur")

        return component
