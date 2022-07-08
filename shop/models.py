from django.db import models
from product.models import Product
from PIL import Image
# Create your models here.


class Shop(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='logo_pics', blank=True, null=True)

    def __str__(self):
        return f'{self.name} market'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.logo.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.logo.path)


class ShopItem(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    count = models.IntegerField()
    price = models.FloatField(max_length=100)

    def __str__(self):
        return f'{self.id} item'


