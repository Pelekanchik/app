from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title': 'Home - Головна',
        'content': 'Магазин мебели HOME'
        
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home - Про нас',
        'content': 'Про нас',
        'text_on_page': "Інформація про нашу фірму і про якість продукції "
        
    }

    return render(request, 'main/about.html', context)
