from django.db import models


# Create your models here.

class product(models.Model):
    product_name=models.CharField(max_length=50)
    product_price=models.IntegerField()
    year_reg=models.CharField(max_length=50)
    product_image=models.ImageField(upload_to="olx/media",null=True,blank=True)
    product_desc=models.CharField(max_length=50)

    def __str__(self):
        return self.product_name
