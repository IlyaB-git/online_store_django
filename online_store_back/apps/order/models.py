from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from catalog.models import Product


class OrderStatus(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    date_create = models.DateField(auto_now_add=True)
    date_confirmed = models.DateField(null=True, blank=True)
    # shipping_id = models.ForeignKey()
    status = models.ForeignKey(OrderStatus, on_delete=models.PROTECT, default=1)
    price = models.PositiveIntegerField()
    comment = models.CharField(max_length=255)

    def __str__(self):
        return str(self.date)

    def get_absolute_url(self):
        return reverse('order', kwargs={'order_id': self.pk})


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='orders')
    count = models.PositiveIntegerField()
