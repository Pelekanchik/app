from django.urls import path
from tovaru import views

app_name = 'tovaru'

urlpatterns = [
    path('', views.catalog, name='index'),
    path('product/', views.product, name='product'),
]
