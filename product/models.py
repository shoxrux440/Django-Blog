from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from PIL import Image
# Create your models here.


class Category(MPTTModel):
    title = models.CharField(max_length=200)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        return f'{self.title}'


class Product(models.Model):
    title = models.CharField(max_length=200)
    subcategory = models.ForeignKey(Category, default='none', on_delete=models.CASCADE, related_name='subcat')
    category = models.ForeignKey(Category, default='none', on_delete=models.CASCADE)
    characteristics = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=200, null=True, blank=True)
    picture = models.ImageField(upload_to='product_logo', null=True, blank=True)

    def __str__(self):
        return f'{self.title}'


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.picture.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.picture.path)