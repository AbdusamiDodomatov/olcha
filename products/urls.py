from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, RatingViewSet

app_name = 'products'

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'ratings', RatingViewSet, basename='ratings')

urlpatterns = [
    path('', include(router.urls)),
]
