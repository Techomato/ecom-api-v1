from typing import Optional

from pydantic import BaseModel

from products.utils.helpers import validate_filter_product_request_data


class FilterProductRequestType(BaseModel):
    category: Optional[str] = None
    subcategory: Optional[str] = None
    brand: Optional[str] = None
    max_price: Optional[int] = None
    min_price: Optional[int] = None
    rating: Optional[int] = None

    def __init__(self, **kwargs):
        validate_filter_product_request_data(data=kwargs)

        super().__init__(**kwargs)
