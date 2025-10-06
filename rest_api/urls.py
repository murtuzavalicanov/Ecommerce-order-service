from django.urls import path, include
# from rest_framework.routers import DefaultRouter
from . import views


# router = DefaultRouter()
# router.register(r'orders', OrderViewSet, basename='order')
# router.register(r'order-items', OrderItemViewSet, basename="order-items")


urlpatterns = [
    # path("", include(router.urls)),
    path('orders/', views.orders_list_create, name='orders_list_create'),
    path('orders/<int:pk>/', views.orders_detail, name='orders_detail'),
]
