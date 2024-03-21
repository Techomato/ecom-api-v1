from typing import Optional

from pydantic import BaseModel

from products.models.db_models.category import Category
from products.utils.helpers import validate_category


class FilterProductRequestType(BaseModel):
    category: Optional[str] = None
    subcategory: Optional[str] = None
    brand: Optional[str] = None
    max_price: Optional[str] = None
    min_price: Optional[str] = None
    rating: Optional[str] = None

    def __init__(self, **kwargs):
        # validate_category(category=kwargs)

        super().__init__(**kwargs)

