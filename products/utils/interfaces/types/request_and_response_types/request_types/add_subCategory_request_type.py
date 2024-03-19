from typing import Optional
from pydantic import BaseModel
from products.models.db_models.category import Category
from products.models.db_models.sub_category import SubCategory
from products.utils.helpers import validate_subCategory


class AddSubCategoryRequestType(BaseModel):
    sub_category_name: str
    category_name: str
    image: Optional[str] = None
    description: Optional[str] = None

    def __init__(self, **kwargs):
        validate_subCategory(data=kwargs)

        super().__init__(**kwargs)

    def save_to_db(self):
        category_type: Category = Category.objects.get(name=self.category_name)
        sub_category: SubCategory = SubCategory()
        sub_category.category = category_type
        sub_category.name = self.sub_category_name
        sub_category.product_image = self.image
        sub_category.description = self.description
        sub_category.save()
