from pydantic import BaseModel

from ecom_exceptions.ecom_exceptions import ECOMValueError
from products.utils.helpers import is_valid_uuid


class RemoveProductRequestType(BaseModel):
    product_id: str

    def __init__(self, **kwargs):
        if not kwargs.get("product_id") or not is_valid_uuid(kwargs.get("product_id")):
            raise ECOMValueError(msg="Product ID is invalid")
        super().__init__(**kwargs)
