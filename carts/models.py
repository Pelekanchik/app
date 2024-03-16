from django.db import models
from tovaru.models import Products

from users.models import User


class CartQueryset(models.QuerySet):
    
    def total_price(self):
        return sum(cart.products_price() for cart in self)        #загальна сума тоару

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)       
        return 0


class Cart(models.Model):

    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Користувач')
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Кількість')
    session_key = models.CharField(max_length=32, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавлення')


    class Meta: 
        db_table = 'cart'
        verbose_name = "Кошик"
        verbose_name_plural = "Кошик"

    objects = CartQueryset().as_manager()    

    def products_price(self):
        return round(self.product.sell_price() * self.quantity, 2)    


    def __str__(self):
        if self.user:
            return f'Кошик {self.user.username} | Товар {self.product.name} | Кількість {self.quantity}'

        return f'Анонітна корзина | Товар {self.product.name} | Кількість {self.quantity}'    