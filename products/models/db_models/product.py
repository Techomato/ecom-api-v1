from django.db import models

from products.models.db_models.abstruct_product import AbstractProduct


class Product(AbstractProduct):
    attribute_name = models.CharField(max_length=100)
