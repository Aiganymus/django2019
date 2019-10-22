from django.db import models

from core.choices import PRODUCT_SIZES, PRODUCT_MEDIUM, PRODUCT_TYPES, PRODUCT_FOOD, SERVICE_TYPES, SERVICE_DELIVERY


class ProductServiceBase(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(max_length=500)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('-price',)
        abstract = True


class Product(ProductServiceBase):
    size = models.PositiveSmallIntegerField(choices=PRODUCT_SIZES, default=PRODUCT_MEDIUM)
    type = models.PositiveSmallIntegerField(choices=PRODUCT_TYPES, default=PRODUCT_FOOD)
    existence = models.BooleanField(default=True)


class Service(ProductServiceBase):
    service_type = models.PositiveSmallIntegerField(choices=SERVICE_TYPES, default=SERVICE_DELIVERY)
    approximate_duration = models.IntegerField()
