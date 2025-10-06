from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import OrderViewSet, OrderItemViewSet

router = SimpleRouter()
router.register(r"orders", OrderViewSet, basename="orders")
router.register(r"order-items", OrderItemViewSet, basename="order-items")

urlpatterns = [
    path("", include(router.urls)),
    path("", include('rest_api.urls'))
]
