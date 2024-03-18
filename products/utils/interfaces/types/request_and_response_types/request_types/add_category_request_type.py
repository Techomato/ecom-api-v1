from typing import Optional

from pydantic import BaseModel

from products.models.db_models.category import Category
from products.utils.helpers import validate_category


class AddCategoryRequestType(BaseModel):
    category_name: str
    image: Optional[str] = None
    description: Optional[str] = None

    def __init__(self, **kwargs):
        validate_category(category=kwargs)

        super().__init__(**kwargs)

    def save_to_db(self):
        category: Category = Category()
        category.name = self.category_name
        category.product_image = self.image
        category.description = self.description
        category.save()
        pass
