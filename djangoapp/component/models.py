from django.db import models

class Component(models.Model):
    name = models.CharField(max_length=50)
    brand = models.ForeignKey(
        'Brand',
        on_delete=models.CASCADE,
    )
    # price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        abstract = True

class Brand(models.Model):
    name = models.CharField(max_length=50)

class Processor(Component):
    frequency = models.FloatField()#Ghz
    cores = models.IntegerField()
    socket = models.ForeignKey(
        'Socket',
        on_delete=models.CASCADE,
    )

class Motherboard(Component):
    ramSlots = models.IntegerField()
    maxRam = models.IntegerField()# Go
    socket = models.ForeignKey(
        'Socket',
        on_delete=models.CASCADE,
    )

class Socket(models.Model):
    name = models.CharField(max_length=50)

class Ram(Component):
    capacity = models.IntegerField()# Go par barrette, capacity * quantity = total memory
    quantity = models.IntegerField()# nombre de barrette
    ramtype = models.ForeignKey(
        'RamType',
        on_delete=models.CASCADE,
    )
    frequency = models.ForeignKey(
        'RamFrequency',
        on_delete=models.CASCADE,
    )

class RamFrequency(models.Model):
    frequency = models.IntegerField()# Mhz

class RamType(models.Model):
    typeName = models.CharField(max_length=10)# DDR2, DDR3, DDR4
