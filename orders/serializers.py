from rest_framework import serializers
from .models import Order, Favorite
from products.models import Product
from products.serializers import ProductSerializer



class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'product', 'quantity', 'status', 'ordered_at']


class FavoriteSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Favorite
        fields = ['user', 'product']
