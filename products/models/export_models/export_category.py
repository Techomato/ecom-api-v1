import datetime
import typing
from typing import Optional
from uuid import UUID
from pydantic import BaseModel

from products.models.db_models.sub_category import SubCategory
from products.models.export_models.export_subcategory import ExportECOMSubCategoryList, ExportECOMSubCategory


class ExportECOMCategory(BaseModel):
    id: Optional[UUID]
    name: Optional[str]
    product_image: Optional[str]
    description: Optional[str]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    sub_category: ExportECOMSubCategoryList

    def __init__(self, **kwargs):
        sub_categories = SubCategory.objects.filter(category__id=kwargs.get('id'))
        sub_cat_list = ExportECOMSubCategoryList(
            sub_category_list=[
                ExportECOMSubCategory(**sub_cat.model_to_dict())
                for sub_cat in sub_categories
            ]
        )
        kwargs["sub_category"] = sub_cat_list

        super().__init__(**kwargs)


class ExportECOMCategoryList(BaseModel):
    category_list: typing.List[ExportECOMCategory]
