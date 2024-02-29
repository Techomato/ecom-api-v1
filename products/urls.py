from django.urls import path

from products.views.all_products import AllProduct

urlpatterns = [
    # Product Paths
    path("all-products", AllProduct.as_view(), name="all-products"),
]
