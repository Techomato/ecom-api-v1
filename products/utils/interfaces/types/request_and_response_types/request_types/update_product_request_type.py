from typing import Optional, List
from _decimal import Decimal
from django.core.exceptions import ObjectDoesNotExist

from pydantic import BaseModel

from ecom_exceptions.ecom_exceptions import ECOMValueError, ProductNotFoundError
from products.models.db_models.category import Category
from products.models.db_models.product import Product
from products.models.db_models.sub_category import SubCategory
from products.utils.helpers import is_valid_uuid, validate_update_request_product_data


class UpdateProductRequestType(BaseModel):
    id: str
    product_name: Optional[str] = None
    brand: Optional[str] = None
    count_in_stock: Optional[int] = None
    category: Optional[str] = None
    description: Optional[str] = None
    subcategory: Optional[str] = None
    image: Optional[str] = None
    product_image_list: Optional[List[str]] = None
    actual_price: Optional[Decimal] = None
    offer_price: Optional[Decimal] = None

    def __init__(self, **kwargs):
        if not kwargs.get("id") or not is_valid_uuid(kwargs.get("id")):
            raise ECOMValueError(msg="Product ID is invalid")

        validate_update_request_product_data(kwargs)
        super().__init__(**kwargs)

    def update_product_in_db(self, seller_id):
        try:
            product = Product.objects.get(id=self.id, seller_id=seller_id)
            if self.category:
                category_type = Category.objects.get(name=self.category)
                product.category = category_type
            if self.subcategory:
                sub_category_type: SubCategory = SubCategory.objects.get(
                    name=self.subcategory
                )
                product.subCategory = sub_category_type

            if self.product_name:
                product.name = self.product_name

            if self.brand:
                product.brand = self.brand

            if self.count_in_stock:
                product.countInStock = self.count_in_stock

            if self.image:
                product.product_image = self.image

            if self.product_image_list:
                product.product_image_list = self.product_image_list

            if self.description:
                product.description = self.description

            if self.actual_price:
                if not isinstance(self.actual_price, Decimal):
                    self.actual_price = Decimal(self.actual_price)
                product.actual_price = self.actual_price

            if self.offer_price:
                if not isinstance(self.offer_price, Decimal):
                    self.offer_price = Decimal(self.offer_price)
                product.offer_price = self.offer_price

            product.save()

        except ObjectDoesNotExist:
            raise ProductNotFoundError()
