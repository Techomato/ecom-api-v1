import json
from typing import Optional, List

from _decimal import Decimal
from pydantic import BaseModel

from ecom_exceptions.ecom_exceptions import ECOMValueError
from products.models.db_models.category import Category
from products.models.db_models.product import Product
from products.models.db_models.sub_category import SubCategory


class CreateProductRequestType(BaseModel):
    name: str
    product_image: str
    product_image_list: Optional[List[str]] = None
    brand: str
    category: Optional[str]
    subCategory: Optional[str]
    description: Optional[str] = None
    actual_price: Decimal
    offer_price: Optional[Decimal] = None
    countInStock: int

    def __init__(self, **kwargs):
        if not kwargs.get("name") or len(kwargs.get("name")) < 5:
            raise ECOMValueError("Product name should have length more than 5")

        if not kwargs.get("product_image"):
            raise ECOMValueError("Product image is required")

        if kwargs.get("product_image_list") and isinstance(
            kwargs.get("product_image_list"), list
        ):
            kwargs["product_image_list"] = json.dumps(kwargs.get("product_image_list"))

        if not kwargs.get("brand"):
            raise ECOMValueError("Brand Name is required")

        if not kwargs.get("category"):
            raise ECOMValueError("Category Name is required")

        if not kwargs.get("subCategory"):
            raise ECOMValueError("Sub Category Name is required")

        if not kwargs.get("description"):
            raise ECOMValueError("Description is required")

        if kwargs.get("actual_price"):
            if isinstance(kwargs.get("actual_price"), str):
                kwargs["actual_price"] = kwargs.get("actual_price").strip(' "')
            actual_price = Decimal(kwargs.get("actual_price"))
            if actual_price <= 0:
                raise ECOMValueError("Actual Price can not be zero or negative")
        else:
            raise ECOMValueError("Actual Price is required")

        if kwargs.get("offer_price"):
            if isinstance(kwargs.get("offer_price"), str):
                kwargs["offer_price"] = kwargs.get("offer_price").strip(' "')
            offer_price = Decimal(kwargs.get("offer_price"))
            if offer_price <= 0:
                raise ECOMValueError("Offer Price can not be zero or negative")
            if kwargs.get("offer_price") > kwargs.get("actual_price"):
                raise ECOMValueError("Offer Price can not be grater than actual price")
        else:
            raise ECOMValueError("Offer Price is required")

        if not kwargs.get("countInStock") or int(kwargs.get("countInStock")) <= 0:
            raise ECOMValueError("Offer Price can not be zero or negative")

        super().__init__(**kwargs)

    def save_to_db(self, seller_id):
        category_type = Category.objects.filter(name=self.category).first()
        if not category_type:
            raise ECOMValueError("Category is not listed")

        sub_category_type: SubCategory = SubCategory.objects.filter(
            name=self.subCategory
        ).first()
        if not sub_category_type:
            raise ECOMValueError("Sub Category is not listed")
        elif sub_category_type.category != category_type:
            raise ECOMValueError("Category & Sub Category are not matching")
        self.category = None
        self.subCategory = None
        product: Product = Product(**self.model_dump())
        product.seller_id = seller_id
        product.category = category_type
        product.subCategory = sub_category_type
        product.save()
