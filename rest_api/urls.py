from django.urls import path
from . import views


urlpatterns = [
    path('orders/', views.orders_list_create, name='orders_list_create'),
    path('order-items/', views.orderitems_list_create, name='orderitems_list_create'),

    path('orders/<int:pk>/', views.orders_detail, name='orders_detail'),
    path('order-items/<int:pk>/', views.orderitems_detail, name='orderitems_detail'),

    path('orders-from-shopcart/', views.create_order_from_shopcart, name='orders_from_shopcart'),

    path('order-items/<int:pk>/status/', views.update_order_item_status, name='update-orderitem-status'),
    
]
