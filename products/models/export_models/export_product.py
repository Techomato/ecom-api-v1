import datetime
import typing
from typing import Optional
from uuid import UUID
from decimal import Decimal
from pydantic import BaseModel

from products.models.export_models.export_category import ExportECOMProductCategory
from products.models.export_models.export_subcategory import (
    ExportECOMProductSubCategory,
)


class ExportECOMProduct(BaseModel):
    id: UUID
    seller_id: str
    name: str
    product_image: str
    product_image_list: Optional[list]
    brand: str
    category: Optional[ExportECOMProductCategory]
    subCategory: Optional[ExportECOMProductSubCategory]
    description: str
    rating: Optional[Decimal]
    numReviews: Optional[int]
    actual_price: Decimal
    offer_price: Optional[Decimal]
    countInStock: int
    created_at: datetime.datetime
    updated_at: datetime.datetime

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ExportECOMProductList(BaseModel):
    product_list: typing.List[ExportECOMProduct]
