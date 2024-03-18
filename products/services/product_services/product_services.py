from django.core.exceptions import ObjectDoesNotExist
from psycopg2 import DatabaseError
from rest_framework.request import Request
from ecom_exceptions.ecom_exceptions import ProductNotFoundError
from products.models.db_models.product import Product
from products.models.export_models.export_product import (
    ExportECOMProduct,
    ExportECOMProductList,
)
from products.services.auth_services.seller_services import SellerServices
from products.utils.interfaces.types.request_and_response_types.request_types.add_subCategory_request_type import \
    AddSubCategoryRequestType
from products.utils.interfaces.types.request_and_response_types.request_types.create_product_request_type import (
    CreateProductRequestType,
)
from products.utils.interfaces.types.request_and_response_types.request_types.remove_product_request_type import (
    RemoveProductRequestType,
)
from products.utils.interfaces.types.request_and_response_types.request_types.update_product_request_type import (
    UpdateProductRequestType,
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
        seller_id = SellerServices().get_seller_id(request=request)
        request_data.save_to_db(seller_id=seller_id)
        return ResponseData(successMessage="Product has been added successfully.")

    def remove_product_service(
        self, request_data: RemoveProductRequestType, request: Request
    ) -> ResponseData:
        seller_id = SellerServices().get_seller_id(request=request)
        self._remove_product_from_db_service(
            product_id=request_data.product_id, seller_id=seller_id
        )
        return ResponseData(successMessage="Product has been removed successfully.")

    def _remove_product_from_db_service(self, product_id: str, seller_id: str):
        try:
            product = Product.objects.get(id=product_id, seller_id=seller_id)

            product.delete()
        except ObjectDoesNotExist:
            raise ProductNotFoundError()

    def update_product_service(
        self, request_data: UpdateProductRequestType, request: Request
    ) -> ResponseData:
        seller_id = SellerServices().get_seller_id(request=request)
        request_data.update_product_in_db(seller_id=seller_id)
        return ResponseData(successMessage="Product has been updated successfully.")

    def add_subCategory_service(
        self, request_data: AddSubCategoryRequestType, request: Request
    ) -> ResponseData:
        seller_id = SellerServices().get_seller_id(request=request)
        if seller_id:
            request_data.save_to_db(seller_id=seller_id)
        return ResponseData(successMessage="Sub Category has been added successfully.")
