from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny  # prod-da öz permission-ların
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def getData(request):
    order={'id':'1','name':'order1'}
    return Response(order)



# class OrderViewSet(viewsets.ModelViewSet):
#     queryset = Order.objects.all().order_by("-id")
#     serializer_class = OrderSerializer
#     permission_classes = [AllowAny]


# class OrderItemViewSet(viewsets.ModelViewSet):
#     queryset = OrderItem.objects.select_related("order").all().order_by("-id")
#     serializer_class = OrderItemSerializer
#     permission_classes = [AllowAny]
