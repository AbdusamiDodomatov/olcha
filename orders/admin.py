# orders/admin.py
from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity', 'status', 'ordered_at')
    list_filter = ('status', 'ordered_at')
    search_fields = ('user__email', 'product__name')

admin.site.register(Order, OrderAdmin)
