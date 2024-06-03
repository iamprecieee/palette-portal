from django.db.models import (Model, CharField, EmailField, DateTimeField,
                              Index, PositiveIntegerField, DecimalField, BooleanField,
                              ForeignKey, CASCADE)
from palette.models import Artwork


class Order(Model):
    first_name = CharField(max_length=200)
    last_name = CharField(max_length=200)
    email = EmailField()
    address = CharField(max_length=250)
    postal_code = CharField(max_length=50)
    city = CharField(max_length=200)
    paid = BooleanField(default=False)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created']
        indexes = [Index(fields=['-created']),
            Index(fields=['email'])]
        
    def __str__(self):
        return f' Order {self.id}'
    
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
    
    
class Item(Model):
    order = ForeignKey(Order, related_name='items', on_delete=CASCADE)
    artwork = ForeignKey(Artwork, related_name='order_items', on_delete=CASCADE)
    price = DecimalField(max_digits=9, decimal_places=2)
    quantity = PositiveIntegerField(default=1)
    
    def __str__(self):
        return f'Item {str(self.id)}'
    
    def get_cost(self):
        return self.price * self.quantity