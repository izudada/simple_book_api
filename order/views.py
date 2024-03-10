from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from order.models import Order

from order.serializers import (
    CreateOrderSerializer,
    ListOrderSerializer,
    UpdateOrderSerializer
)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ListOrderSerializer

    def create(self, request):
        serializer = CreateOrderSerializer(data=request.data) 
        if serializer.is_valid():  
            serializer.save(
                user=request.user,
                data=serializer.validated_data
            )
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        
    def update(self, request, pk, partial=False):
        instance = self.get_object()
        serializer = UpdateOrderSerializer(
            data=request.data, 
            context={
                'user': request.user,
                'order': instance
            },
            partial=partial
        )

        if serializer.is_valid():
            serializer.save(
                data={
                    'state': serializer.validated_data['state'], 
                    'orders': serializer.validated_data['orders']
                },
                instance=instance,
            )
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        instance = self.get_object()
        if request.user != instance.user:
            return Response(
                {'error': 'You are not authorized to perform this action'}, 
                status.HTTP_400_BAD_REQUEST
            )
        return Response(
            {'success': 'Order successfully deleted'},
            status.HTTP_204_NO_CONTENT
        )
