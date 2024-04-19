from django.shortcuts import render

from .models import Product


# Create your views here.
def index(request):
    product_list = Product.objects.all()
    context = {
        "product_list": product_list,
    }
    return render(request, "myapp/index.html", context)


def product(request, id):
    try:
        product = Product.objects.get(id=id)
    except:
        product = None
    context = {
        "product": product,
    }
    return render(request, "myapp/show.html", context)
