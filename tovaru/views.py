from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, render


from tovaru.models import Products
from tovaru.utils import q_search


def catalog(request, category_slug=None):

    page = request.GET.get("page", 1)
    on_sale = request.GET.get("on_sale", None)
    order_by = request.GET.get("order_by", None)
    query = request.GET.get('q', None)

    if category_slug == "all":
        tovaru = Products.objects.all()
    elif query:
        tovaru = q_search(query)
    else:
        tovaru = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    if on_sale:
        tovaru = tovaru.filter(discount__gt=0)

    if order_by and order_by != "default":
        tovaru = tovaru.order_by(order_by)

    paginator = Paginator(tovaru,9)
    current_page = paginator.page(int(page))

    context = {
        "title": "Home - Каталог",
        "tovaru": current_page,
        "slug_url": category_slug
    }
    return render(request, "tovaru/catalog.html", context)


def product(request, product_slug):

    product = Products.objects.get(slug=product_slug)  

    context = {"product": product}

    return render(request, "tovaru/product.html", context=context)
