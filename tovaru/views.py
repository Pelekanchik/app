from django.shortcuts import render
from django.template import context

from tovaru.models import Products 

def catalog(request):

    tovaru = Products.objects.all()

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
