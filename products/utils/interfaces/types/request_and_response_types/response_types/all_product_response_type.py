from products.models.export_models.export_product import ExportECOMProductList
from products.utils.interfaces.types.request_and_response_types.response_types.base_response_type import (
    ResponseData,
)


class AllProductResponseData(ResponseData):
    data: ExportECOMProductList
