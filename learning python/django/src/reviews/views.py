from django.shortcuts import render

from django.views.generic import (
    ListView,
)

from .models import Reviews

# Create your views here.
class ReviewListView(ListView):
    template_name = "reviews/reviews.html"
    queryset = Reviews.objects.all()