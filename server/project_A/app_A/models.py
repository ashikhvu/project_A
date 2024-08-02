from django.db import models

class Products(models.Model):
    product_name = models.CharField(max_length=255)
    product_qty = models.IntegerField(blank=True,null=True)
    price = models.IntegerField(blank=True,null=True)
    image = models.ImageField(upload_to='downloads',blank=True,null=True)



