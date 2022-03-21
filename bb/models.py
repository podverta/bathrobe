from django.db import models

class Item(models.Model):
    """items for embroidery"""
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        """return name"""
        return self.name

class Sample(models.Model):
    type = models.ForeignKey(Item, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, unique=True)
    color = models.CharField(max_length=20)
    size = models.CharField(max_length=20)
    quantity = models.IntegerField
    comments = models.TextField

    def __str__(self):
        return self.name