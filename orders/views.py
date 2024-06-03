from django.shortcuts import render, redirect
from .forms import OrderCreateForm, Order
from.models import Item
from cart.cart import Cart
from django.db.transaction import atomic


def create_order(request):
    cart = Cart(request)
    if request.method == 'POST':
        if len(cart) == 0:
            error_message = 'No items found in cart'
            return render(request, 'error/400.html', {'error_message': error_message,
                                                      'remove_subheader': True, 'return_url': 'cart:cart-detail'}) 
            
        form = OrderCreateForm(request.POST)
        
        if form.is_valid():
            with atomic():
                order = form.save()
                for item in cart:
                    Item.objects.create(order=order, artwork=item['artwork'],
                                        price=item['price'], quantity=item['quantity'])
                cart.clear()
            return redirect('orders:order-created', order_id=order.id)
        
        error_message = '\n'.join(
            [f'{", ".join(errors)}' for field, errors in form.errors.items()])
        return render(request, 'error/400.html', {'error_message': error_message,
                                                  'remove_subheader': True, 'return_url': 'orders:order-create'})
        
    if len(cart) == 0:
            error_message = 'No items found in cart'
            return render(request, 'error/400.html', {'error_message': error_message,
                                                      'remove_subheader': True, 'return_url': 'cart:cart-detail'}) 
            
    form = OrderCreateForm()
    return render(request, 'order/create.html', {'form': form, 'show_subheader': False})


def order_created(request, order_id):
    order = Order.objects.filter(id=order_id).first()
    if not order:
        return render(request, 'error/404.html',
                   {'error_message': 'An error occured during order retrieval',
                     'remove_subheader': True})
    
    return render(request, 'order/created.html', {'order': order,
                                                  'show_subheader': False})