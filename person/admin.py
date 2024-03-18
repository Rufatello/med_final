from django.contrib import admin

from person.models import Person, Product, Basket, Comments


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price',)


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product',)


@admin.register(Comments)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product',)

