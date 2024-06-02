from django.urls import path
from .views import cart_detail, add_item, remove_item


app_name = 'cart'


urlpatterns = [
    path('', cart_detail, name='cart-detail'),
    path('add/<int:artwork_id>/', add_item, name='cart-add'),
    path('remove/<int:artwork_id>/', remove_item, name='cart-remove'),
]
