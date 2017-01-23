# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from djangoapp.components.models import Component, Processor, Brand, Socket, HardDrive, HardDriveType, PowerSupply, GraphicCard, PowerSupplyFormFactor, Motherboard, Case, Ram, RamType, RamFrequency, PciType, MotherBoardFormFactor
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

        elif(item['itemType'] == "motherboard"):
            print("Motherboard --")
            component = Motherboard()

            socket = Socket.objects.filter(name__iexact = item['socket'])  # __iexact -> Case-insensitive exact match
            if(socket.count() <= 0): # if socket dont exists
                socket = Socket.objects.create(name=item['socket'])
            else:
                socket = socket[0]
            component.socket = socket

            component.ramSlots = item["ramslots"]
            component.maxRam = item["maxram"]

            ramtype = RamType.objects.filter(typeName__iexact = item['ramtype'])  # __iexact -> Case-insensitive exact match
            if(ramtype.count() <= 0): # if ramtype dont exists
                ramtype = RamType.objects.create(typeName=item['ramtype'])
            else:
                ramtype = ramtype[0]
            component.ramtype = ramtype

            # ramfrequency = RamFrequency.objects.filter(frequency = item['ramfrequency'][0])
            # if(ramfrequency.count() <= 0): # if ramtype dont exists
            #     ramfrequency = RamFrequency.objects.create(frequency = item['ramfrequency'][0])
            # else:
            #     ramfrequency = ramfrequency[0]
            # component.frequency = ramfrequency

            # pcitype = PciType.objects.filter(name__iexact = item['pcitypes'][0])
            # if(pcitype.count() <= 0):
            #     pcitype = PciType.objects.create(name = item['pcitypes'][0])
            # else:
            #     pcitype = pcitype[0]
            # component.pcitypes = pcitype

            formfactor = MotherBoardFormFactor.objects.filter(name = item['formfactor'])
            if(formfactor.count() <= 0):
                formfactor = MotherBoardFormFactor.objects.create(name = item['formfactor'])
            else:
                formfactor = formfactor[0]
            component.formfactor = formfactor

        elif(item['itemType'] == "ram"):
            component = Ram()

            component.capacity = item["capacity"]
            component.quantity = item["quantity"]

            ramtype = RamType.objects.filter(typeName__iexact = item['ramtype'])  # __iexact -> Case-insensitive exact match
            if(ramtype.count() <= 0): # if ramtype dont exists
                ramtype = RamType.objects.create(typeName=item['ramtype'])
            else:
                ramtype = ramtype[0]
            component.ramtype = ramtype

            frequency = RamFrequency.objects.filter(frequency = item['frequency'])
            if(frequency.count() <= 0): # if ramtype dont exists
                frequency = RamFrequency.objects.create(frequency = item['frequency'])
            else:
                frequency = frequency[0]
            component.frequency = frequency

        elif(item['itemType'] == "case"):
            component = Case()

            component.weight = item["weight"]
            component.width = item["width"]
            component.height = item["height"]
            component.depth = item["depth"]

            formfactor = PowerSupplyFormFactor.objects.filter(name__iexact = item['powersupplyformfactor'])  # __iexact -> Case-insensitive exact match
            if(formfactor.count() <= 0):
                formfactor = PowerSupplyFormFactor.objects.create(name=item['powersupplyformfactor'])
            else:
                formfactor = formfactor[0]
            component.powerSupplyFormFactor = formfactor

        elif(item['itemType'] == "graphiccard"):
            component = GraphicCard()

            component.memory = item["memory"]

            pcitype = PciType.objects.filter(name__iexact = item['pcitype'])  # __iexact -> Case-insensitive exact match
            if(pcitype.count() <= 0):
                pcitype = PciType.objects.create(name = item['pcitype'])
            else:
                pcitype = pcitype[0]
            component.pcitype = pcitype

        elif(item['itemType'] == "harddrive"):
            component = HardDrive()

            component.capacity = item["capacity"]

            hardDriveType = HardDriveType.objects.filter(name__iexact = item['harddrivetype'])  # __iexact -> Case-insensitive exact match
            if(hardDriveType.count() <= 0):
                hardDriveType = HardDriveType.objects.create(name = item['harddrivetype'])
            else:
                hardDriveType = hardDriveType[0]
            component.hardDriveType = hardDriveType

        elif(item['itemType'] == "powersupply"):
            component = PowerSupply()

            component.watts = item["watts"]
            component.modular = item["modular"]

            formfactor = PowerSupplyFormFactor.objects.filter(name__iexact = item['factorForm'])  # __iexact -> Case-insensitive exact match
            if(formfactor.count() <= 0):
                formfactor = PowerSupplyFormFactor.objects.create(name=item['factorForm'])
            else:
                formfactor = formfactor[0]
            component.factorForm = formfactor


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
