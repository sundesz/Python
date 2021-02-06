from django.db import models
from datetime import datetime
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    is_active = models.BooleanField(default=True)
    # created = models.DateTimeField(default=datetime.now)
    # updated = models.DateTimeField(default=datetime.now)

    def get_absolute_url(self):
        return f"/blog/{self.id}/"
        # return reverse("article-update", kwargs={"id": self.id})

    def get_delete_url(self):
        return f"/blog/{self.id}/delete/"
