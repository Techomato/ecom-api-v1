from products.models.export_models.export_category import ExportECOMCategoryList
from products.utils.interfaces.types.request_and_response_types.response_types.base_response_type import (
    ResponseData,
)


class AllCategorySubcategoryResponseData(ResponseData):
    data: ExportECOMCategoryList
