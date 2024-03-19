import datetime
from typing import Optional, List
from uuid import UUID
from pydantic import BaseModel


class ExportECOMSubCategory(BaseModel):
    id: Optional[UUID]
    name: Optional[str]
    product_image: Optional[str]
    description: Optional[str]
    created_at: datetime.datetime
    updated_at: datetime.datetime


class ExportECOMSubCategoryList(BaseModel):
    sub_category_list: Optional[List[ExportECOMSubCategory]] = None
