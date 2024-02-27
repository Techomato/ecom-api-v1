from django.db import models

from products.models.db_models.base_model.base_model import ECOMBaseModel
from products.models.db_models.category import Category


class SubCategory(ECOMBaseModel):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=False, blank=False)
    product_image = models.CharField(max_length=2000, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
