from django.shortcuts import render, get_object_or_404
from .models import Product, SmartPhone, Sale


def home(request):
    """
    home page
    adding sales and random (most popular) produce fro each category
    :param request: request
    :return: render home page
    """
    sales = Sale.objects.all()

    context = {
        "smartphones": SmartPhone.objects.all(),
    }

    if sales:
        context["first_sale"] = Sale.objects.all()[0]
    if len(sales) > 1:
        context["sales"] = Sale.objects.all()[1:]

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
