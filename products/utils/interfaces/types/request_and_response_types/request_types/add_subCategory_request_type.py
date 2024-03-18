from typing import Optional, List

from _decimal import Decimal
from pydantic import BaseModel

from ecom_exceptions.ecom_exceptions import ECOMValueError
from products.models.db_models.category import Category
from products.models.db_models.product import Product
from products.models.db_models.sub_category import SubCategory


class AddSubCategoryRequestType(BaseModel):
    sub_category_name: str
    category_name: str
    image: Optional[str] = None
    description: Optional[str] = None

    def __init__(self, **kwargs):

        if not kwargs.get("sub_category_name"):
            raise ECOMValueError(msg="Sub Category name is required")
        if not kwargs.get("category_name"):
            raise ECOMValueError(msg="Category name is required")
        #
        # if not kwargs.get("product_image") or len(kwargs.get("product_image")) < 9:
        #     raise ECOMValueError(msg="Product image is required")
        #
        # if not kwargs.get("brand"):
        #     raise ECOMValueError(msg="Brand Name is required")
        #
        # if not kwargs.get("category"):
        #     raise ECOMValueError(msg="Category Name is required")
        #
        # if not kwargs.get("subCategory"):
        #     raise ECOMValueError(msg="Sub Category Name is required")
        #
        # if not kwargs.get("description"):
        #     raise ECOMValueError(msg="Description is required")
        #
        # if kwargs.get("actual_price"):
        #     if isinstance(kwargs.get("actual_price"), str):
        #         kwargs["actual_price"] = kwargs.get("actual_price").strip(' "')
        #     actual_price = Decimal(kwargs.get("actual_price"))
        #     if actual_price <= 0:
        #         raise ECOMValueError(msg="Actual Price can not be zero or negative")
        #     if actual_price >= 1000000:
        #         raise ECOMValueError(msg="Price can not be greater than Rs.9,99,999")
        # else:
        #     raise ECOMValueError(msg="Actual Price is required")
        #
        # if kwargs.get("offer_price"):
        #     if isinstance(kwargs.get("offer_price"), str):
        #         kwargs["offer_price"] = kwargs.get("offer_price").strip(' "')
        #     offer_price = Decimal(kwargs.get("offer_price"))
        #     if offer_price <= 0:
        #         raise ECOMValueError(msg="Offer Price can not be zero or negative")
        #     if kwargs.get("offer_price") > kwargs.get("actual_price"):
        #         raise ECOMValueError(
        #             msg="Offer Price can not be grater than actual price"
        #         )
        # else:
        #     raise ECOMValueError(msg="Offer Price is required")
        #
        # if not kwargs.get("countInStock") or int(kwargs.get("countInStock")) <= 0:
        #     raise ECOMValueError(msg="Product quantity can not be zero or negative")

        super().__init__(**kwargs)

    def save_to_db(self, seller_id):
        sub_category: SubCategory = SubCategory()
        # sub_category.category = self.category_name
        sub_category.name = self.sub_category_name
        sub_category.product_image = self.image
        sub_category.description = self.description
        # sub_category.save()
        pass
