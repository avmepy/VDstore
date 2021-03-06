from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.views.generic import View
from .models import SmartPhone, Sale, SmartWatch, Tablet, Computer, Audio, Laptop, Product, Cart, User, Profile, Comment

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



def product_detail(request, product_id):

    sub_classes = [SmartPhone, SmartWatch, Tablet, Computer, Audio, Laptop, Product]

    product = None
    product_with_comments = get_object_or_404(Product, id=product_id)

    for sub_class in sub_classes:
        try:
            product = sub_class.objects.get(id=product_id)

            break
        except:
            continue

    context = {
        'product_with_comments': product_with_comments,
        'product': product,
        'product_model': product.__class__._meta.model_name,
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


@login_required
def add_to_cart(request, product_id):
    if request.method == "POST":
        user = request.user

        item = get_object_or_404(Product, id=product_id)
        try:
            cur_cart = Cart.objects.get(user=Profile.objects.get(user=user))
        except:
            cur_cart = Cart(user=Profile.objects.get(user=user))
            cur_cart.save()
        cur_cart.products.add(item)
        return product_detail(request, product_id)

    return HttpResponse("something went wrong :(")


@login_required
def my_cart(request):
    user = request.user
    cur_cart = None
    try:
        cur_cart = Cart.objects.get(user=Profile.objects.get(user=user))
    except:
        cur_cart = Cart(user=Profile.objects.get(user=user))
        cur_cart.save()

    if request.method == "POST":
        if "clear" in request.POST:
            cur_cart.products.clear()

        if "buy" in request.POST:

            return render(request, 'store/pay.html',
                          context={"price": sum([product.price for product in cur_cart.products.all()])})

    context = {
        "current": list(cur_cart.products.all()),
        "summary_price": sum([product.price for product in cur_cart.products.all()])
    }

    return render(request, 'store/cart.html', context=context)


def create_comment(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        new_comment = Comment.objects.create(
            author=request.user,
            product=product,
            text=request.POST['comment-text']
        )
        new_comment.save()

        return redirect('store:product_detail_url', product_id)