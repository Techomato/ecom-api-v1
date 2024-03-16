from django.urls import path

from products.views.all_products import AllProduct
from products.views.create_product import CreatProductView
from products.views.remove_product import RemoveProductView

urlpatterns = [
    # Product Paths
    path("all-products", AllProduct.as_view(), name="all-products"),
    path("add-product", CreatProductView.as_view(), name="add-product"),
    path("remove-product", RemoveProductView.as_view(), name="remove-product"),
]
