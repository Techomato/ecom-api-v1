import json
from django.db import models

from products.models.db_models.base_model.base_model import ECOMBaseModel
from products.models.db_models.category import Category
from products.models.db_models.sub_category import SubCategory


class AbstractProduct(ECOMBaseModel):
    seller_id = models.CharField(max_length=200, null=False, blank=False)
    name = models.CharField(max_length=200, null=False, blank=False)
    product_image = models.CharField(max_length=2000, null=True, blank=True)
    product_image_list = models.CharField(max_length=5000, null=True, blank=True)
    brand = models.CharField(max_length=200, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    subCategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True, blank=True)
    rating = models.DecimalField(
        null=True, blank=True, default=0, decimal_places=3, max_digits=5
    )
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    actual_price = models.DecimalField(
        max_digits=8, decimal_places=2, null=False, blank=False
    )
    offer_price = models.DecimalField(
        max_digits=8, decimal_places=2, null=False, blank=False
    )
    countInStock = models.IntegerField(null=False, default=0, blank=False)

    class Meta:
        abstract = True

    def save(self, **kwargs):
        if kwargs.get("product_image_list") and not isinstance(
            kwargs.get("product_image_list"), str
        ):
            kwargs["product_image_list"] = json.dumps(kwargs.get("product_image_list"))
        super().save(**kwargs)
