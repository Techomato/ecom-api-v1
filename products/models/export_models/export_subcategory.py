import datetime
import typing
from typing import Optional
from uuid import UUID
from pydantic import BaseModel

from products.models.export_models.export_category import ExportECOMCategory


class ExportECOMSubCategory(BaseModel):
    id: Optional[UUID]
    name: Optional[str]
    category: Optional[ExportECOMCategory]
    product_image: Optional[str]
    description: Optional[str]
    created_at: datetime.datetime
    updated_at: datetime.datetime

    def __init__(self, **kwargs):
        if kwargs.get("category"):
            kwargs["category"] = ExportECOMCategory(
                **kwargs.get("category").model_to_dict()
            )
        super().__init__(**kwargs)


class ExportECOMSubCategoryList(BaseModel):
    sub_category_list: typing.List[ExportECOMSubCategory]
