from django.urls import path
from .views import (
    article_create_view,
    article_index_view,
    article_update_view,
    article_delete_view,
)

app_name = "article"

urlpatterns = [
    path("", article_index_view, name="article-index"),
    path("create/", article_create_view, name="article-create"),
    path("<int:id>/", article_update_view, name="article-update"),
    path("<int:id>/delete/", article_delete_view, name="article-delete"),
]