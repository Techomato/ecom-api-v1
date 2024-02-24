from uuid import UUID

from django.db import models

from products.models.db_models.base_model.base_model import ECOMBaseModel


class AbstructProduct(ECOMBaseModel):

    seller_id = models.CharField(max_length=200,null=False, blank=False)
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to="images/products/", null=True, blank=True)
    brand = models.CharField(max_length=200, null=True, blank=True)
    # category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    # subCategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True, blank=True)
    rating = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    mrp = models.DecimalField(max_digits=8, decimal_places=2)
    offer_price = models.DecimalField(max_digits=8, decimal_places=2)
    countInStock = models.IntegerField(null=False, default=0)
    
    class Meta:
        abstract = True