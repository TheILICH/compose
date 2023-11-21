from django.db import models


class Item(models.Model):
    name = models.CharField(null=True, max_length=100, default='', blank=True)
    price = models.IntegerField(null=True, default='', blank=True)

    def __str__(self):
        return f'name = {self.name} and price = {self.price}'

