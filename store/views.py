from django.shortcuts import render, get_object_or_404
from .models import Product, SmartPhone, Sale


def home(request):
    context = {"smartphones": SmartPhone.objects.all(),
               }
    #            "first_sale": Sale.objects.all()[0],
    #            "sales": Sale.objects.all()[1:]}

    return render(request, "store/home.html", context=context)


def product_detail(request, slug):

    product = get_object_or_404(Product, slug=slug)

    context = {
        'product': product,
    }

    # TODO: write template "store/templates/store/product_detail.html"
    return render(request, 'store/product_detail.html', context=context)


def products_list(request):

    products = Product.objects.all()

    context = {
        'products': products
    }

    # TODO: write template "store/templates/store/product_detail.html"
    return render(request, '', context=context)
