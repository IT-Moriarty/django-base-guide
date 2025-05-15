from os import name
from django.contrib import admin
from.models import Category, Product


@admin.register(Category)
class CategoryAdmon(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug' : ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'avaliable', 'created', 'updated']

    list_filter = ['avaliable', 'created', 'updated', 'category']
    list_editable = ['price', 'avaliable']
    prepopulated_fields = {'slug' : ('name',)}

