from typing import Optional, List
from _decimal import Decimal

from pydantic import BaseModel

from ecom_exceptions.ecom_exceptions import ECOMValueError
from products.utils.helpers import is_valid_uuid


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
        super().__init__(**kwargs)
