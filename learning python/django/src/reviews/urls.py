from django.urls import path

from .views import (
    ReviewListView,
)

app_name = "reviews"

urlpatterns = [
    path("", ReviewListView.as_view(), name="article-list"),
    # path("create/", article_create_view, name="article-create"),
    # path("<int:id>/", article_update_view, name="article-update"),
    # path("<int:id>/delete/", article_delete_view, name="article-delete"),
]