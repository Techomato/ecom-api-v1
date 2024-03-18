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
        # if not kwargs.get("name") or len(kwargs.get("name")) < 5:
        #     raise ECOMValueError(msg="Product name should have length more than 5")
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
        # category_type = Category.objects.filter(name=self.category).first()
        # if not category_type:
        #     raise ECOMValueError(msg="Category is not listed")
        #
        # sub_category_type: SubCategory = SubCategory.objects.filter(
        #     name=self.subCategory
        # ).first()
        # if not sub_category_type:
        #     raise ECOMValueError(msg="Sub Category is not listed")
        # elif sub_category_type.category != category_type:
        #     raise ECOMValueError(msg="Category & Sub Category are not matching")
        # self.category = None
        # self.subCategory = None
        # product: Product = Product(**self.model_dump())
        # product.seller_id = seller_id
        # product.category = category_type
        # product.subCategory = sub_category_type
        # product.save()
        pass