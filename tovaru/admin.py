from django.contrib import admin

from tovaru.models import Categories, Products

# admin.site.register(Categories)
# admin.site.register(Products)


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = [
        "name",
    ]


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):  # настройка адмін панелі
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "quantity", "price", "discount"]
    list_editable = ["discount",]
    search_fields = ["name", "description"]
    list_filter = ["discount", "quantity", "category"]
    fields = [
        "name",
        "category",
        ("price", "discount"),
        "quantity",
        "image",
        "description",
        "slug",
    ]
