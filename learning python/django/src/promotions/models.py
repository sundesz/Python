from django.db import models
from datetime import datetime
from django.urls import reverse

# Create your models here.
class Promotions(models.Model):
    name = models.CharField(max_length=100)
    promotion_type = models.CharField(max_length=12)
    description = models.TextField()
    effective_date = models.DateTimeField(null=True, default=datetime.now)
    expiration_date = models.DateTimeField(null=True, default=datetime.now)
    is_active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("promotions:promotion-view")

    def get_absolute_url_update(self):
        return reverse("promotions:promotion-update", kwargs={"id": self.id})

    def get_absolute_url_delete(self):
        return reverse("promotions:promotion-delete", kwargs={"id": self.id})
