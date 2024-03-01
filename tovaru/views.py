from django.shortcuts import render

from tovaru.models import Products 


def catalog(request, category_slug):

    if category_slug == 'all':
        tovaru = Products.objects.all()
    else:
        tovaru = Products.objects.filter(category__slug=category_slug)


    context = {
        'title': 'home - Каталог',
        'tovaru': tovaru,
    }
    return render(request, 'tovaru/catalog.html', context)


def product(request, product_slug):

    product = Products.objects.get(slug=product_slug)     #ми отримуємо всю інформацію по конкретному товару по slug

    context = {
        'product': product
    }
    
    return render(request, 'tovaru/product.html', context=context)
