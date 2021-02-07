from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse
from django.http import HttpResponse

from .models import Promotions
from .forms import PromotionForm

# Create your views here.
class PromotionsView(ListView):
    template_name = "promotions/promotions.html"
    queryset = Promotions.objects.all()


class PromotionCreateView(CreateView):
    template_name = "promotions/promotion_create.html"
    form_class = PromotionForm
    queryset = Promotions.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)


class PromotionUpdateView(UpdateView):
    template_name = "promotions/promotion_update.html"
    form_class = PromotionForm

    def get_object(self):
        _id = self.kwargs.get("id")
        return get_object_or_404(Promotions, id=_id)

    def from_valid(self, form):
        return super().form_valid(form)


class PromotionDeleteView(DeleteView):
    template_name = "promotions/promotion_delete.html"

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Promotions, id=id_)

    def get_success_url(self):
        return reverse("promotions:promotion-view")