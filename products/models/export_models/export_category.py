import datetime
import typing
from typing import Optional
from uuid import UUID
from pydantic import BaseModel


class ExportECOMCategory(BaseModel):
    id: Optional[UUID]
    name: Optional[str]
    product_image: Optional[str]
    description: Optional[str]
    created_at: datetime.datetime
    updated_at: datetime.datetime

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ExportECOMCategoryList(BaseModel):
    category_list: typing.List[ExportECOMCategory]
