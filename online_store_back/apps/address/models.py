from django.db import models
from django.contrib.auth.models import User

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='address')
    phone = models.CharField(max_length=15)
    first_name = models.CharField(max_length=32)
    second_name = models.CharField(max_length=32)
    patronymic = models.CharField(max_length=32)
    region = models.CharField(max_length=32)
    district = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    street_room = models.CharField(max_length=128)
    index = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адресы'