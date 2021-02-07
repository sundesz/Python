from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime

# Create your models here.
class Reviews(models.Model):
    name = models.CharField(max_length=100)
    # product_id = models.CharField(max_length=100)
    description = models.TextField(null=True)
    rating = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0),
        ],
    )
    created = models.DateTimeField(default=datetime.now)

    def get_absolute_url(self):
        return reverse("reviews:review-detail", kwargs={"id": self.id})

    def get_absolute_url_update(self):
        return reverse("reviews:review-update", kwargs={"id": self.id})
        # return f"{self.id}/"

    def get_absolute_url_delete(self):
        return reverse("reviews:review-delete", kwargs={"id": self.id})

    def get_absolute_url_review(self):
        return reverse("reviews:review-list")
