from django.core.exceptions import ObjectDoesNotExist
from psycopg2 import DatabaseError
from rest_framework.request import Request
from ecom_exceptions.ecom_exceptions import ProductNotFoundError, ECOMValueError
from products.models.db_models.category import Category
from products.models.db_models.product import Product
from products.models.db_models.sub_category import SubCategory
from products.models.export_models.export_product import (
    ExportECOMProduct,
    ExportECOMProductList,
)
from products.services.auth_services.seller_services import SellerServices
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
        try:
            seller_id = SellerServices().get_seller_id(request=request)
            product = Product.objects.get(id=request_data.id, seller_id=seller_id)
            category_type = Category.objects.filter(name=request_data.category).first()
            sub_category_type: SubCategory = SubCategory.objects.filter(
                name=request_data.subcategory
            ).first()

            if product:
                if request_data.product_name:
                    product.name = request_data.product_name

                if request_data.brand:
                    product.brand = request_data.brand

                if request_data.count_in_stock:
                    product.countInStock = request_data.count_in_stock

                if request_data.category:
                    if not category_type:
                        raise ECOMValueError(msg="Category is not listed")
                    else:
                        product.category.name = request_data.category

                if request_data.subcategory:
                    if not sub_category_type:
                        raise ECOMValueError(msg="Sub Category is not listed")
                    elif sub_category_type.category != category_type:
                        raise ECOMValueError(
                            msg="Category & Sub Category are not matching"
                        )
                    else:
                        product.subCategory.name = request_data.subcategory

                if request_data.image:
                    product.product_image = request_data.image

                if request_data.product_image_list:
                    product.product_image_list = request_data.product_image_list

                if request_data.description:
                    product.description = request_data.description

                if request_data.actual_price:
                    if request_data.actual_price <= 0:
                        raise ECOMValueError(
                            msg="Actual Price can not be zero or negative"
                        )
                    if request_data.actual_price >= 1000000:
                        raise ECOMValueError(
                            msg="Price can not be greater than Rs.9,99,999"
                        )
                    else:
                        product.actual_price = request_data.actual_price

                if request_data.offer_price:
                    if request_data.offer_price > product.actual_price:
                        raise ECOMValueError(
                            msg="Offer Price can not be grater than actual price"
                        )
                    else:
                        product.offer_price = request_data.offer_price

                product.save()
            return ResponseData(successMessage="Product has been updated successfully.")

        except ObjectDoesNotExist:
            raise ProductNotFoundError()
