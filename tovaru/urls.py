from django.urls import path
from tovaru import views

app_name = 'tovaru'

urlpatterns = [
    path('<slug:category_slug>/', views.catalog, name='index'),
    path('product/<slug:product_slug>/', views.product, name='product'),
]
