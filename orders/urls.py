from django.urls import path
from .views import create_order, order_created


app_name = 'orders'


urlpatterns = [
    path('create/', create_order, name='create-order'),
    path('created/<int:order_id>/', order_created, name='order-created'),
]
