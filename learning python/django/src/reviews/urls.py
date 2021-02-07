from django.urls import path

from .views import (
    ReviewListView,
    ReviewDetailView,
    ReviewCreateView,
    ReviewUpdateView,
    ReviewDeleteView,
)

app_name = "reviews"

urlpatterns = [
    path("", ReviewListView.as_view(), name="review-list"),
    # path("<int:pk>/", ReviewDetailView.as_view(), name="review-update"),
    path("create/", ReviewCreateView.as_view(), name="review-create"),
    path("<int:id>/", ReviewDetailView.as_view(), name="review-detail"),
    path("<int:id>/update/", ReviewUpdateView.as_view(), name="review-update"),
    path("<int:id>/delete/", ReviewDeleteView.as_view(), name="review-delete"),
]