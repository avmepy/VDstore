from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from .models import SmartPhone, Sale, SmartWatch, Tablet, Computer, Audio, Laptop, Product, Comment
import random


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


def show_category(request, product):
    items = {
        "smartphones": SmartPhone.objects.all(),
        "smartwatches": SmartWatch.objects.all(),
        "tablets": Tablet.objects.all(),
        "computers": Computer.objects.all(),
        "audios": Audio.objects.all(),
        "laptops": Laptop.objects.all()
    }

    current = items[product]

    context = {'current': current}
    return render(request, 'store/category.html', context=context)


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