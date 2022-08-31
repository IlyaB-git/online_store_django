from django.db import models
from django.contrib.auth.models import User
from catalog.models import Product

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1)

    # def __str__(self):
    #     return self.count

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'