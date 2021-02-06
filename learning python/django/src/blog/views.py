from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ArticleForm
from .models import Article

# Create your views here.
def article_index_view(request):
    article_list = Article.objects.all()

    context = {
        "object_list": article_list,
    }

    return render(request, "articles/article_index.html", context)


def article_update_view(request, id):
    try:
        obj = Article.objects.get(id=id)
        form = ArticleForm(request.POST or None, instance=obj)

        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect("../")

        context = {
            "form": form,
        }
    except Article.DoesNotExist:
        raise Http404

    return render(request, "articles/article_detail.html", context)


def article_create_view(request):
    form = ArticleForm()
    if request.method == "POST":
        form = ArticleForm(request.POST or None)

        if form.is_valid():
            # Article.objects.create(form.cleaned_data)
            form.save()
            return redirect("../")
        else:
            print(form.errors())

    context = {
        "form": form,
    }

    return render(request, "articles/article_create.html", context)


def article_delete_view(request, id):
    obj = get_object_or_404(Article, id=id)

    if request.method == "POST":
        obj.delete()
        return redirect("../../")

    return render(request, "articles/article_delete.html", {})