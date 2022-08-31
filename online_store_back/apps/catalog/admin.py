from django.contrib import admin
from .models import Category, Vendor, Product, Product_image

admin.site.register(Category)
admin.site.register(Vendor)
admin.site.register(Product)
admin.site.register(Product_image)