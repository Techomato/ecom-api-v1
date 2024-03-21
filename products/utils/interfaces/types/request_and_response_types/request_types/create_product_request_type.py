from typing import Optional, List

from _decimal import Decimal
from pydantic import BaseModel

from ecom_exceptions.ecom_exceptions import ECOMValueError
from products.models.db_models.category import Category
from products.models.db_models.product import Product
from products.models.db_models.sub_category import SubCategory
from products.utils.helpers import validate_add_request_product_data


class CreateProductRequestType(BaseModel):
    name: str
    product_image: str
    brand: str
    category: str
    subCategory: str
    actual_price: Decimal
    offer_price: Decimal
    countInStock: int
    description: Optional[str] = None
    offer_price: Optional[Decimal] = None
    product_image_list: Optional[List[str]] = None

    def __init__(self, **kwargs):
        validate_add_request_product_data(data=kwargs)

        super().__init__(**kwargs)

    def save_to_db(self, seller_id):
        category_type = Category.objects.filter(name=self.category).first()
        if not category_type:
            raise ECOMValueError(msg="Category is not listed")

        sub_category_type: SubCategory = SubCategory.objects.filter(
            name=self.subCategory
        ).first()
        if not sub_category_type:
            raise ECOMValueError(msg="Sub Category is not listed")
        elif sub_category_type.category != category_type:
            raise ECOMValueError(msg="Category & Sub Category are not matching")
        self.category = None
        self.subCategory = None
        product: Product = Product(**self.model_dump())
        product.seller_id = seller_id
        product.category = category_type
        product.subCategory = sub_category_type
        product.save()
