from django.db import models
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
