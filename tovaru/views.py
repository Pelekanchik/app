from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, render

from tovaru.models import Products 


def catalog(request, category_slug, page=1):

    if category_slug == 'all':
        tovaru = Products.objects.all()
    else:
        tovaru = get_list_or_404(Products.objects.filter(category__slug=category_slug))


    paginator = Paginator(tovaru, 6)
    current_page = paginator.page(page)

    context = {
        'title': 'home - Каталог',
        'tovaru': current_page,
        "slug_url": category_slug,
    }
    return render(request, 'tovaru/catalog.html', context)


def product(request, product_slug):

    product = Products.objects.get(slug=product_slug)     #ми отримуємо всю інформацію по конкретному товару по slug

    context = {
        'product': product
    }
    
    return render(request, 'tovaru/product.html', context=context)
