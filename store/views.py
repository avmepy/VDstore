from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import SmartPhone, Sale, SmartWatch, Tablet, Computer, Audio, Laptop, Product
import random


MAX_PRICE = 1e7


def home(request):
    """
    home page
    adding sales and random (most popular) produce fro each category
    :param request: request
    :return: render home page
    """
    # getting all sales
    sales = Sale.objects.all()

    # getting all produce
    produce = list(SmartPhone.objects.all()) + list(SmartWatch.objects.all()) + list(Tablet.objects.all()) + \
              list(Computer.objects.all()) + list(Audio.objects.all()) + list(Laptop.objects.all())

    random.shuffle(produce)  # shuffle produce

    if len(produce) > 6:
        produce = produce[:6]  # get 6 random products to represent on home page

    context = {
        "produce": produce
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

    return render(request, 'store/product_detail.html', context=context)


def show_category(request, product):
    items = {
        "smartphones": SmartPhone,
        "smartwatches": SmartWatch,
        "tablets": Tablet,
        "computers": Computer,
        "audios": Audio,
        "laptops": Laptop
    }

    brands = list(set([item.brand for item in items[product].objects.all()]))  # to be unique

    if request.method == "POST":

        # --- price ---

        price_from = request.POST["from"]
        price_to = request.POST["to"]


        try:
            price_from = int(price_from)
        except Exception:
            price_from = 0

        try:
            price_to = int(price_to)
        except Exception:
            price_to = MAX_PRICE

        # --- price ---

        # --- brand ---

        chosen_brands = [brand for brand in brands if brand in request.POST]

        if not chosen_brands:
            chosen_brands = brands

        # --- brand ---

        current = items[product].objects.filter(price__range=[price_from, price_to], brand__in=chosen_brands)

    else:
        current = items[product].objects.all()

    context = {'current': current, "name": product, "brands": brands}

    return render(request, 'store/category.html', context=context)
