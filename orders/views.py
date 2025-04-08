from rest_framework import viewsets, permissions
from .models import Order, Favorite
from .serializers import OrderSerializer, FavoriteSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.select_related('user', 'product').all()
    serializer_class = OrderSerializer


class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
