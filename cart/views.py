from django.shortcuts import render, redirect
from .cart import Cart, Artwork
from django.views.decorators.http import require_POST
from .forms import CartUpdateForm


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_form'] = CartUpdateForm(
            initial={'quantity': item['quantity'], 'override': True}
        )
    
    return render(request, 'cart/detail.html', {'cart': cart,
                                                'show_subheader': False})
    

@require_POST 
def add_item(request, artwork_id):
    cart = Cart(request)
    form = CartUpdateForm(request.POST)
    artwork = Artwork.available.filter(id=artwork_id).first()
    if form.is_valid():
        cart.add(artwork, form.cleaned_data['quantity'],
                 form.cleaned_data['override'])
        
    return redirect('cart:cart-detail')


@require_POST 
def remove_item(request, artwork_id):
    cart = Cart(request)
    artwork = Artwork.available.filter(id=artwork_id).first()
    cart.remove(artwork)
        
    return redirect('cart:cart-detail')