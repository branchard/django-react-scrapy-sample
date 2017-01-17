from django.db import models
from scrapy_djangoitem import DjangoItem


class Component(models.Model):
    name = models.CharField(max_length=50)
    brand = models.ForeignKey(
        'Brand',
        on_delete=models.CASCADE,
    )

    # class Meta:
    #     abstract = True


class Brand(models.Model):
    name = models.CharField(max_length=50)


class Processor(Component):
    frequency = models.FloatField()  # Ghz
    cores = models.IntegerField()
    socket = models.ForeignKey(
        'Socket',
        on_delete=models.CASCADE,
    )


class Motherboard(Component):
    ramSlots = models.IntegerField()
    maxRam = models.IntegerField()  # Go
    ramtype = models.ForeignKey(
        'RamType',
        on_delete=models.CASCADE,
    )
    ramfrequency = models.ManyToManyField("RamFrequency")  # une carte mere est compatible avec plusieurs frequences de ram
    socket = models.ForeignKey(
        'Socket',
        on_delete=models.CASCADE,
    )
    pcitypes = models.ManyToManyField("PciType")  # une carte mere peut avoir plusieurs slots PCI
    formfactor = models.ForeignKey(
        'MotherBoardFormFactor',
        on_delete=models.CASCADE,
    )


class Socket(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return "{{id: {}, name: {}}}".format(self.id, self.name)


class Ram(Component):
    capacity = models.IntegerField()  # Go par barrette, capacity * quantity = total memory
    quantity = models.IntegerField()  # nombre de barrette
    ramtype = models.ForeignKey(
        'RamType',
        on_delete=models.CASCADE,
    )
    frequency = models.ForeignKey(
        'RamFrequency',
        on_delete=models.CASCADE,
    )


class RamFrequency(models.Model):
    frequency = models.IntegerField()  # Mhz


class RamType(models.Model):
    typeName = models.CharField(max_length=10)  # DDR2, DDR3, DDR4


class GraphicCard(Component):
    memory = models.IntegerField()  # Go
    pcitype = models.ForeignKey(
        'PciType',
        on_delete=models.CASCADE,
    )


class PciType(models.Model):
    name = models.CharField(max_length=50)  # PCI-E 3.0, PCI-E 2.0


class Case(Component):
    weight = models.FloatField()  # in Kg
    width = models.IntegerField()  # in mm
    height = models.IntegerField()  # in mm
    depth = models.IntegerField()  # in mm
    motherBoardFormFactors = models.ManyToManyField("MotherBoardFormFactor")  # un boitier peut etre compatible avec plusieurs Carte mere
    powerSupplyFormFactor = models.ForeignKey(
        'PowerSupplyFormFactor',
        on_delete=models.CASCADE,
    )


class MotherBoardFormFactor(models.Model):
    name = models.CharField(max_length=10)


class PowerSupply(Component):
    watts = models.IntegerField()  # in watt
    modular = models.BooleanField()
    factorForm = models.ForeignKey(
        'PowerSupplyFormFactor',
        on_delete=models.CASCADE,
    )


class PowerSupplyFormFactor(models.Model):
    name = models.CharField(max_length=10)


class HardDrive(Component):
    capacity = models.IntegerField()  # Go
    hardDriveType = models.ForeignKey(
        'HardDriveType',
        on_delete=models.CASCADE,
    )


class HardDriveType(models.Model):
    name = models.CharField(max_length=10)  # SSD ou HDD
