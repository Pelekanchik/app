from django.shortcuts import redirect, render
from carts.models import Cart

from tovaru.models import Products


def cart_add(request, product_slug):
    
    product = Products.objects.get(slug=product_slug)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)

        if carts.exists():                                     # якщо товар є в корзині добавиться ще один додатково
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1) 

    return redirect(request.META['HTTP_REFERER'])

def cart_change(request, product_slug):
    ...    

def cart_remove(request, cart_id):
    
    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    return redirect(request.META['HTTP_REFERER'])