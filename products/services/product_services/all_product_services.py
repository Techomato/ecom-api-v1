from psycopg2 import DatabaseError

from products.models.db_models.product import Product
from products.models.export_models.export_product import (
    ExportECOMProduct,
    ExportECOMProductList,
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
