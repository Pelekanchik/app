from django.shortcuts import render

def catalog(request):
    return render(request, 'tovaru/catalog.html')


def product(request):
    return render(request, 'tovaru/product.html')
