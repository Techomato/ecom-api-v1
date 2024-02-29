import datetime
import typing
from typing import Optional
from uuid import UUID
from pydantic import BaseModel

from products.models.export_models.export_category import ExportECOMProductCategory


class ExportECOMProductSubCategory(BaseModel):
    id: Optional[UUID]
    name: Optional[str]
    category: Optional[ExportECOMProductCategory]
    product_image: Optional[str]
    description: Optional[str]
    created_at: datetime.datetime
    updated_at: datetime.datetime

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ExportECOMProductSubCategoryList(BaseModel):
    sub_category_list: typing.List[ExportECOMProductSubCategory]
