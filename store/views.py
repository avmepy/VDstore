from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.views.generic import View
from .models import SmartPhone, Sale, SmartWatch, Tablet, Computer, Audio, Laptop, Product, Cart, User
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


class ShowCategory(View):

    def _prep(self, product):
        items = {
            "smartphones": SmartPhone,
            "smartwatches": SmartWatch,
            "tablets": Tablet,
            "computers": Computer,
            "audios": Audio,
            "laptops": Laptop
        }

        try:
            price_from = list(items[product].objects.order_by("price"))[0].price
        except Exception:
            price_from = 0

        try:
            price_to = list(items[product].objects.order_by("price"))[-1].price
        except Exception:
            price_to = 1e7
        chosen_brands = []
        brands = sorted(list(set([item.brand for item in items[product].objects.all()])))  # to be unique

        return items, price_from, price_to, chosen_brands, brands

    def get(self, request, product):
        items, price_from, price_to, chosen_brands, brands = ShowCategory._prep(self, product)

        current = items[product].objects.all()
        context = {'current': current,
                   "name": product,
                   "brands": brands,
                   "chosen_brands": chosen_brands,
                   "price_from": price_from,
                   "price_to": price_to
                   }
        return render(request, 'store/category.html', context=context)

    def post(self, request, product):

        items, price_from, price_to, chosen_brands, brands = ShowCategory._prep(self, product)
        # --- price ---
        try:
            price_from = int(request.POST["from"])
        except Exception:
            pass

        try:
            price_to = int(request.POST["to"])
        except Exception:
            pass
        # --- price ---

        # --- brand ---
        chosen_brands = [brand for brand in brands if brand in request.POST]

        if not chosen_brands:
            chosen_brands = brands

        # --- brand ---

        current = items[product].objects.filter(price__range=[price_from, price_to], brand__in=chosen_brands)
        context = {'current': current,
                   "name": product,
                   "brands": brands,
                   "chosen_brands": chosen_brands,
                   "price_from": price_from,
                   "price_to": price_to
                   }
        return render(request, 'store/category.html', context=context)


def add_to_cart(request, slug, product_id):
    if request.method == "POST":
        print("added")
        item = SmartPhone.objects.get(id=product_id)
        print(item)

        return product_detail(request, slug)

    return HttpResponse("something went wrong :(")
