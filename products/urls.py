from django.urls import path

from products.views import Hello

urlpatterns = [
    # User Paths
    path("hello", Hello.as_view(), name="hello"),
]
