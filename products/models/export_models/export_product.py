import datetime
import typing
from typing import Optional
from uuid import UUID
from decimal import Decimal
from pydantic import BaseModel

from products.models.export_models.export_category import ExportECOMCategory
from products.models.export_models.export_subcategory import (
    ExportECOMSubCategory,
)


class ExportECOMProduct(BaseModel):
    id: UUID
    seller_id: str
    name: str
    product_image: str
    product_image_list: Optional[list]
    brand: str
    category: Optional[ExportECOMCategory]
    subCategory: Optional[ExportECOMSubCategory]
    description: str
    rating: Optional[Decimal]
    numReviews: Optional[int]
    actual_price: Decimal
    offer_price: Optional[Decimal]
    countInStock: int
    created_at: datetime.datetime
    updated_at: datetime.datetime

    def __init__(self, **kwargs):
        if kwargs.get("category"):
            kwargs["category"] = ExportECOMCategory(
                **kwargs.get("category").model_to_dict()
            )
        if kwargs.get("subCategory"):
            kwargs["subCategory"] = ExportECOMSubCategory(
                **kwargs.get("subCategory").model_to_dict()
            )
        super().__init__(**kwargs)


class ExportECOMProductList(BaseModel):
    product_list: typing.List[ExportECOMProduct]
