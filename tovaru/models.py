from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Назва')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table= 'category'
        verbose_name = 'Категорію'
        verbose_name_plural = 'Категорії'

    def __str__(self):
         return self.name  


class Products(models.Model):
        name = models.CharField(max_length=150, unique=True, verbose_name='Назва')
        slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
        description = models.TextField(blank=True, null=True, verbose_name='Описання')
        image = models.ImageField(upload_to='tovaru_images',blank=True, null=True, verbose_name='Зображення')
        price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Ціна')
        discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Скидка в %')
        quantity = models.PositiveIntegerField(default=0, verbose_name='Кількість')
        catigory = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категорія')

 
        class Meta:
            db_table= 'product'
            verbose_name = 'Деталь'
            verbose_name_plural = 'Деталі'

        
        def __str__(self):
         return f'{self.name} Кількість - {self.quantity}'