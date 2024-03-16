from django.db import models

from products.models.db_models.base_model.base_model import ECOMBaseModel


class Category(ECOMBaseModel):
    name = models.CharField(max_length=200, null=False, blank=False)
    product_image = models.CharField(max_length=2000, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
