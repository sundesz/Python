from django.urls import path
from .views import (
    PromotionsView,
    PromotionCreateView,
    PromotionUpdateView,
    PromotionDeleteView,
)

app_name = "promotions"
urlpatterns = [
    path("", PromotionsView.as_view(), name="promotion-view"),
    path("create/", PromotionCreateView.as_view(), name="promotion-create"),
    path("<int:id>/update/", PromotionUpdateView.as_view(), name="promotion-update"),
    path("<int:id>/delete/", PromotionDeleteView.as_view(), name="promotion-delete"),
]
