from django import forms

from .models import Product


class ProductForm(forms.ModelForm):

    title = forms.CharField(
        label="Titles",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your title",
            }
        ),
    )

    email = forms.EmailField()

    class Meta:
        model = Product
        fields = [
            "title",
            "description",
            "price",
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")

        if not "title" in title:
            raise forms.ValidationError("This is not a valid title")

        return title

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")

        if not email.endswith("edu"):
            raise forms.ValidationError("This is not a valid email")

        return email


class RawProductForm(forms.Form):
    title = forms.CharField(
        label="Titles",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your title",
            }
        ),
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "id": "descriptionId",
                "class": "my-class",
                "rows": "20",
                "columns": "40",
            }
        ),
    )
    price = forms.DecimalField(initial=20)
