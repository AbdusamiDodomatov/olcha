from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, FavoriteViewSet

app_name = 'orders'


router = DefaultRouter()
router.register(r'orders', OrderViewSet)
router.register(r'favorites', FavoriteViewSet) 



urlpatterns = [
    path('', include(router.urls)),
]
