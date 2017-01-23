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
        elif(itemType == "Carte mère"):
            itemType = "motherboard"
        elif(itemType == "Mémoire PC"):
            itemType = "ram"
        elif(itemType == "Boîtier PC"):
            itemType = "case"
        elif(itemType == "Carte graphique"):
            itemType = "graphiccard"
        elif(itemType == "Disque dur interne"):
            itemType = "harddrive"
        elif(itemType == "Alimentation PC"):
            itemType = "powersupply"
        else:
            print("Item not recognized")
            return


        parsedItem = self.ldlcParse(response, itemType)
        parsedItem['itemType'] = itemType
        parsedItem['itemDjangoModel'] = itemDjangoModel

        return parsedItem #return item to the pipeline


    def ldlcParse(self, response, itemType):
        specsParent = response.xpath("//table[@id='productParametersList']")
        def getSpec(specName):
            return specsParent.xpath("//td//*[contains(text(),'{}')]/../..//td[2]//*[not(*)]//text()".format(specName))[0].extract()

        component = dict()

        component["price"] = float(response.xpath("//meta[@itemprop='price']/@content")[0].extract().replace(',', '.'))
        component["shopName"] = "ldlc"

        component["name"] = getSpec("Désignation")
        component["brand"] = getSpec("Marque")

        component["photo"] = response.xpath("//img[contains(@id, 'ImgProduct')]/@src")[0].extract()

        if(itemType == "processor"):
            component["frequency"] = float(getSpec("Fréquence CPU").replace("GHz", "").replace(" ", "").replace(",", "."))
            component["cores"] = int(getSpec("Nombre de core"))
            component["socket"] = getSpec("Support du processeur")

        elif(itemType == "motherboard"):
            component["socket"] = getSpec("Support du processeur")
            component["ramslots"] = int(getSpec("Format de mémoire")[0])
            component["maxram"] = int(getSpec("Capacité maximale de RAM").replace(" Go", ""))
            component["ramtype"] = getSpec("Type de mémoire")
            component["ramfrequency"] = [int("1333 MHz".replace(" MHz", ""))] # TODO
            component["pcitypes"] = ["PCI Express 3.0 16x"] # TODO
            component["formfactor"] = "ATX" # TODO

        elif(itemType == "ram"):
            component["capacity"] = int(getSpec("Capacité par barrette").replace(" Go", ""))
            component["quantity"] = int(getSpec("Nombre de barrettes"))
            component["ramtype"] = getSpec("Type de mémoire")
            component["frequency"] = int("1333 MHz".replace(" MHz", "")) # TODO

        elif(itemType == "case"):
            component["weight"] = float(getSpec("Poids").replace(" kg", "").replace(",", "."))
            component["width"] = int(getSpec("Largeur").replace(" mm", ""))
            component["height"] = int(getSpec("Hauteur").replace(" mm", ""))
            component["depth"] = int(getSpec("Profondeur").replace(" mm", ""))
            component["motherboardformfactor"] = ["ATX"] # TODO
            component["powersupplyformfactor"] = "ATX" # TODO

        elif(itemType == "graphiccard"):
            component["memory"] = int(getSpec("Taille mémoire vidéo").replace(" Mo", ""))
            component["pcitype"] = "PCI Express 3.0 16x"

        elif(itemType == "harddrive"):
            capacity = getSpec("Capacité")
            if("To" in capacity):
                capacity = int(capacity.replace(" To", "")) * 1000
            else:
                capacity = int(capacity.replace(" Go", ""))
            component["capacity"] = capacity
            component["harddrivetype"] = getSpec("Type de Disque")

        elif(itemType == "powersupply"):
            component["watts"] = int(getSpec("Puissance").replace(" W", ""))
            component["modular"] = getSpec("Modulaire") == "Oui"
            component["factorForm"] = "ATX"  # TODO



        return component
