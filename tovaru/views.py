from django.shortcuts import render

from tovaru.models import Products 

def catalog(request):

    tovaru = Products.objects.all()

    context = {
        'title': 'home - Каталог',
        'tovaru': tovaru,
    }
    return render(request, 'tovaru/catalog.html', context)


def product(request):
    return render(request, 'tovaru/product.html')
