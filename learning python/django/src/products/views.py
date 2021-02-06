from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ProductForm, RawProductForm
from .models import Product

# Create your views here.


def product_detail_view(request):
    product_list = Product.objects.all()
    context = {
        "object_list": product_list,
    }

    return render(request, "products/product_details.html", context)


# def product_create_view(request):

#     form = RawProductForm()

#     if request.method == "POST":
#         form = RawProductForm(request.POST)

#         if form.is_valid():
#             Product.objects.create(**form.cleaned_data)
#             # print(form.cleaned_data)
#         else:
#             print(form.errors)

#     context = {
#         "form": form,
#     }

#     return render(request, "products/product_create.html", context)


def product_create_view(request):
    initial_data = {
        "title": "Default title",
    }

    obj = Product.objects.get(id=1)

    # form = ProductForm(request.POST or None, initial=initial_data, instance=obj)
    form = ProductForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        "form": form,
    }

    return render(request, "products/product_create.html", context)


def dynamic_lookup_view(request, product_id):
    # obj = get_object_or_404(Product, id=product_id)

    try:
        obj = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        raise Http404

    context = {
        "product": obj,
    }

    return render(request, "products/product_detail.html", context)


def product_delete_view(request, product_id):
    obj = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        obj.delete()
        return redirect("../../")

    context = {
        "object": obj,
    }

    return render(request, "products/product_delete.html", context)
