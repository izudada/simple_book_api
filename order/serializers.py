from rest_framework import serializers

from book.models import Book
from order.models import Order


class SingleOrderSerializer(serializers.Serializer):
    id = serializers.CharField()
    quantity = serializers.IntegerField()


class CreateOrderSerializer(serializers.Serializer):
    orders = SingleOrderSerializer(many=True)
    total_amount = serializers.IntegerField(required=False)


    def validate(self, data):
        total = 0
        for item in data.get('orders'):
            book_id = item.get('id')
            book_exists = Book.objects.filter(id=book_id).exists()

            if book_exists is False:
                raise serializers.ValidationError(
                    f"Book id {item.get('id')} not found "
                )
            book = Book.objects.get(id=book_id)
            if book.qty_left < int(item.get('quantity')):
                raise serializers.ValidationError(f"book quantity {item.get('quantity')} is greater than stock left")
            
            total += (item.get('quantity') * book.price)

        data['total_amount'] = total
        return data
    
    def save(self, user, data):
        order = Order.objects.create(
            user=user,
            meta_data=data
        ).save()
        return order


class ListOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id','user', 'meta_data', 'order_state')
        read_only_fields = ('id', 'user', 'order_state') 


class UpdateOrderSerializer(serializers.Serializer):
    orders = SingleOrderSerializer(many=True)
    state = serializers.CharField()
    total_amount = serializers.IntegerField(required=False)

    def validate(self, data):
        ORDER_STATE_CHOICES = ("OPEN", "CANCELED", "DELIVERED")
        
        state = data.get('state')
        user = self.context['user']
        order = self.context['order']
    
        if user != order.user:
            raise serializers.ValidationError(
                "You are not authorized to perform this action"
            )
        if state and state not in ORDER_STATE_CHOICES:
            raise serializers.ValidationError(
                f"Invalid state choice must be any of {ORDER_STATE_CHOICES}"
            )
        return data
    
    def save(self, data, instance):
        state = data.get('state', '')
        order = data.get('orders', '')

        if state:
            instance.state = state
        if order:
            instance.update_meta_data( order)
        instance.save()
