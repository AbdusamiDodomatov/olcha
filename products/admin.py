from django.contrib import admin
from .models import Category, Product

# Регистрация модели Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # Что будет отображаться в списке
    search_fields = ('name',)  # Поле для поиска
    list_filter = ('name',)  # Фильтры для списка

# Регистрация модели Product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'category')  # Что будет отображаться в списке
    search_fields = ('name', 'category__name')  # Поле для поиска
    list_filter = ('category',)  # Фильтры для списка
