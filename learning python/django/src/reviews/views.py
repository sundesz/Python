from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Reviews
from .forms import ReviewForm

# Create your views here.
class ReviewListView(ListView):
    template_name = "reviews/reviews.html"
    queryset = Reviews.objects.all()


class ReviewDetailView(DetailView):
    template_name = "reviews/review_detail.html"
    # queryset = Reviews.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Reviews, id=id_)


class ReviewUpdateView(UpdateView):
    template_name = "reviews/review_update.html"
    form_class = ReviewForm
    # queryset = Reviews.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Reviews, id=id_)

    def form_valid(self, form):
        return super().form_valid(form)


class ReviewCreateView(CreateView):
    template_name = "reviews/review_create.html"
    form_class = ReviewForm
    queryset = Reviews.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ReviewDeleteView(DeleteView):
    template_name = "reviews/review_delete.html"

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Reviews, id=id_)

    def get_success_url(self):
        return reverse("reviews:review-list")
