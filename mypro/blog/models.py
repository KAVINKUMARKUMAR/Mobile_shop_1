from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=250)
    price=models.IntegerField()
    img=models.ImageField(upload_to='products/')
    stock=models.PositiveBigIntegerField()


    def __str__(self):
        return f"product: {self.name}"