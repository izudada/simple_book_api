from django.db import models

from authentication.models import User
from helpers.models import TrackingModel


class Order(TrackingModel, models.Model):

    ORDER_STATE_CHOICES = [
        ("OPEN", "OPEN"), 
        ("CANCELED", "CANCELED"),
        ("DELIVERED", "DELIVERED")
    ]

    meta_data = models.JSONField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_state = models.CharField(
        max_length=9,
        choices=ORDER_STATE_CHOICES,
        verbose_name="Order state",
        default="OPEN"
    )


    def __str__(self):
        return f"Order for {self.user.username}"
    
    @property
    def total_quantity(self):
        toal_quantity = 0
        for item in self.meta_data:
            toal_quantity += item['quantity']
        return toal_quantity
    
    @property
    def total_amount(self):
        return self.meta_data['total_amount']
    
    def update_meta_data(self, new_orders_data):
        # Retrieve existing meta_data or initialize it if it's empty
        meta_data = self.meta_data or {"orders": [], "total_amount": float('0.00')}
        
        # Update the orders list with the new data
        for new_order in new_orders_data:
            # Check if the order already exists in the meta_data
            for existing_order in meta_data["orders"]:
                print(type(existing_order), new_order, new_orders_data)
                if existing_order["id"] == new_order["id"]:
                    existing_order["quantity"] += new_order["quantity"]
                    break
            else:
                # If the order doesn't exist, add it to the orders list
                meta_data["orders"].append({"id": new_order["id"], "quantity": new_order["quantity"]})

        # Recalculate the total_amount based on the updated orders list
        total_amount = sum(order["quantity"] * float('1000.00') for order in meta_data["orders"])  # Assuming price is $1000 per item
        
        # Update the total_amount in the meta_data
        meta_data["total_amount"] = total_amount
        
        # Save the updated meta_data back to the order instance
        self.meta_data = meta_data
        self.save()

