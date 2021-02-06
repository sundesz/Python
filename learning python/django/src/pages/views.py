from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    print(request.user)
    # return HttpResponse("<h1>Welcome Sandesh !!!!</h1>")
    my_context = {"name": "I am in Home page", "list": [8, 9, 10, "Abc"]}
    return render(request, "home.html", my_context)


def about_view(request, *args, **kwargs):
    # return HttpResponse("<h1>About page</h1")
    my_context = {"name": "I am in About page"}
    return render(request, "about.html", my_context)
