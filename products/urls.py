from django.urls import path

from products.views.add_category import AddCategoryView
from products.views.all_products import AllProduct
from products.views.create_product import CreatProductView
from products.views.remove_product import RemoveProductView
from products.views.update_product import UpdateProductView

urlpatterns = [
    # Product Paths
    path("all-products", AllProduct.as_view(), name="all-products"),
    path("add-product", CreatProductView.as_view(), name="add-product"),
    path("remove-product", RemoveProductView.as_view(), name="remove-product"),
    path("update-product", UpdateProductView.as_view(), name="update-product"),
    path("add-category", AddCategoryView.as_view(), name="add-category"),
]
