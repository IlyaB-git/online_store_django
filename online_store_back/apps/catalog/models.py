from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, unique=True, db_index=True)
    primary_cat = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='categories', blank=True, null=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Vendor(models.Model):
    name = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(max_length=64, unique=True, db_index=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'


class Product(models.Model):
    name = models.CharField(max_length=128)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    vendor = models.ForeignKey(Vendor, on_delete=models.PROTECT, related_name='products', null=True, blank=True)
    price = models.PositiveIntegerField(null=True, blank=True)
    price_discount = models.PositiveIntegerField(null=True, blank=True)
    description = models.TextField()
    properties = models.JSONField()
    is_public = models.BooleanField(default=True, db_index=True)
    count = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class Product_image(models.Model):
    def directory_path_save(instance, filename):
        return 'products/{0}/{1}'.format(instance.product.category.slug, filename)

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=directory_path_save)

    def __str__(self):
        return self.product.name
    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
