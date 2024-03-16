from psycopg2 import DatabaseError
from rest_framework.request import Request

from products.models.db_models.product import Product
from products.models.export_models.export_product import (
    ExportECOMProduct,
    ExportECOMProductList,
)
from products.services.auth_services.seller_services import SellerServices
from products.utils.interfaces.types.request_and_response_types.request_types.create_product_request_type import (
    CreateProductRequestType,
)
from products.utils.interfaces.types.request_and_response_types.response_types.base_response_type import (
    ResponseData,
)


class ProductServices:
    @staticmethod
    def get_all_products_service() -> ExportECOMProductList:
        try:
            get_all_products_from_db = Product.objects.all()
        except Exception:
            raise DatabaseError()
        if get_all_products_from_db:
            all_products_list = []
            for product in get_all_products_from_db:
                product_export = ExportECOMProduct(**product.model_to_dict())
                all_products_list.append(product_export)
            all_products_list = ExportECOMProductList(product_list=all_products_list)
            return all_products_list
        else:
            return ExportECOMProductList(product_list=[])

    @staticmethod
    def create_new_product_service(
        request_data: CreateProductRequestType, request: Request
    ) -> ResponseData:
        sellerID = SellerServices().get_seller_id(request=request)
        request_data.save_to_db(seller_id=sellerID)
        return ResponseData(successMessage="Product has been added successfully.")
