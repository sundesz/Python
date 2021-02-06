from django.urls import path
from .views import (
    product_create_view,
    product_delete_view,
    product_detail_view,
    dynamic_lookup_view,
)

app_name = "products"
urlpatterns = [
    path("", product_detail_view, name="product-list"),
    path("create/", product_create_view, name="product-create"),
    path("<int:product_id>/", dynamic_lookup_view, name="product-detail"),
    path("<int:product_id>/delete/", product_delete_view, name="product-delete"),
]