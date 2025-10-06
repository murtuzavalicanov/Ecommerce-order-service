from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny  # prod-da öz permission-ların
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status



@api_view(['GET', 'POST'])
def orders_list_create(request):
    if request.method == 'GET':
        orders = Order.objects.all().order_by('-id')
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    
@api_view(['GET', 'PATCH', 'DELETE'])
def orders_detail(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        serializer = OrderSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# class OrderViewSet(viewsets.ModelViewSet):
#     queryset = Order.objects.all().order_by("-id")
#     serializer_class = OrderSerializer
#     permission_classes = [AllowAny]


# class OrderItemViewSet(viewsets.ModelViewSet):
#     queryset = OrderItem.objects.select_related("order").all().order_by("-id")
#     serializer_class = OrderItemSerializer
#     permission_classes = [AllowAny]
