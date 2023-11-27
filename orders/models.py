import uuid
from django.db import models
from restaurants.models import Restaurant
from menus.models import FoodItem
# Create your models here.


ORDER_STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('Cooked', 'Cooked'),
    ('Delivered', 'Delivered'),
    ('Cancalled', 'Cancalled'),
]

class Order(models.Model):
    id = models.UUIDField( 
        primary_key = True, 
        default = uuid.uuid4, 
        editable = False) 
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=15)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    order_status = models.CharField(
        max_length=50,
        choices=ORDER_STATUS_CHOICES,
        default='Pending',
    )
    ordered_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name + self.email

    def get_total_price(self):
        items = OrderItem.objects.filter(order = self)
        total_price = 0
        for i in items:
            total_price += i.price
        return total_price
        
class OrderItem(models.Model):
    id = models.UUIDField( 
        primary_key = True, 
        default = uuid.uuid4, 
        editable = False) 
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)



    