from django import forms

from .models import Promotions


class PromotionForm(forms.ModelForm):

    name = forms.CharField(
        label="Promotion name",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Promotion name ..",
            }
        ),
    )

    PROMOTION_CHOICES = (
        (1, "Promotion type 1"),
        (2, "Promotion type 2"),
    )

    promotion_type = forms.ChoiceField(
        label="Promotion type",
        choices=PROMOTION_CHOICES,
    )

    description = forms.CharField(
        label="Description",
        widget=forms.Textarea(
            attrs={
                "placeholder": "Descriptions ...",
                "rows": "3",
                "columns": "60",
            }
        ),
    )

    class Meta:
        model = Promotions
        fields = [
            "name",
            "description",
            "promotion_type",
            "effective_date",
            "expiration_date",
            "is_active",
        ]