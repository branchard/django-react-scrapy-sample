import scrapy
from shopscraper.items import ShopscraperItem, ProcessorItem

class ShopscraperSpider(scrapy.Spider):
    name = "shopscraper"
    allowed_domains = ["www.ldlc.com"]

    def start_requests(self):
        urls = [
            "https://www.ldlc.com/fiche/PB00148533.html",
            "http://www.ldlc.com/fiche/PB00148534.html",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # define item type
        itemType = response.xpath("//ul[contains(@class, 'cheminDeFer')]//li[contains(@class, 'last')]//span//text()").extract()[0]
        if(itemType == "Processeur"):
            itemType = "processor"


        parsedItem = self.ldlcParse(response, itemType)

        if(itemType == "processor"):
            item = ProcessorItem()

        for key, value in parsedItem.items():
            item[key] = value

        # print(item)
        return item #return item to the pipeline

        # for sel in response.xpath('//table[contains(@class, "wikitable")]//tr'):
        #
        #     # On vérifie qu'il ne s'agit pas du header du tableau
        #     nom = sel.xpath('td[1]//text()').extract()
        #     if not nom:
        #         continue
        #
        #     item = WikibeerItem()
        #     item['nom'] = "".join(nom)
        #     item['type'] = "".join(sel.xpath('td[2]//text()').extract())
        #     item['degre'] = "".join(sel.xpath('td[3]//text()').extract())
        #     item['brasserie'] = "".join(sel.xpath('td[4]//text()').extract())
        #
        #     item.save()


    def ldlcParse(self, response, itemType):
        specsParent = response.xpath("//table[@id='productParametersList']")
        def getSpec(specName):
            return specsParent.xpath("//*[contains(text(),'{}')]/../..//td[2]//*[not(*)]//text()".format(specName))[0].extract()

        component = dict()
        component["name"] = getSpec("Désignation")
        component["brand"] = getSpec("Marque")

        if(itemType == "processor"):
            component["frequency"] = float(getSpec("Fréquence CPU").replace("GHz", "").replace(" ", "").replace(",", "."))
            component["cores"] = int(getSpec("Nombre de core"))
            component["socket"] = getSpec("Support du processeur")

        return component
