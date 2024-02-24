from uuid import UUID

from django.db import models

from products.models.db_models.abstruct_product import AbstructProduct
from products.models.db_models.base_model.base_model import ECOMBaseModel


class Product(AbstructProduct):
    attribute_name = models.CharField(max_length=100)
