from django.db import models

from blog.models import Product

from django.contrib.auth.models import User

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    quantity = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} added by {self.user.username} at {self.date_added}"
    def get_total(self):
        return self.product.price * self.quantity

# Create your models here.
