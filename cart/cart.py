from django.conf import settings
from palette.models import Artwork
from decimal import Decimal


class Cart:
    def __init__(self, request):
        ''' 
        Check if cart_session key exists in session, else add a new one.
        Assign the cart_session's value:dict to the `cart` variable.
        '''
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
        
    def add(self, artwork, quantity=1, override_quantity=False):
        artwork_id = str(artwork.id)
        if artwork_id not in self.cart:
            self.cart[artwork_id] = {'price': str(artwork.price),
                                     'quantity': 0}
            
        if override_quantity:
            self.cart[artwork_id]['quantity'] = quantity
        else:
            self.cart[artwork_id]['quantity'] += quantity
            
        self.save()
        
    def save(self):
        self.session.modified = True
        
    def remove(self, artwork):
        ''' 
        Remove item from cart.
        '''
        artwork_id = str(artwork.id)
        if artwork_id in self.cart:
            del self.cart[artwork_id]
            
            self.save()
            
    def __iter__(self):
        ''' 
        Create a copy of the cart_session to add artworks and
        calculate pricing data to/fro cart_session's value.
        '''
        artwork_ids = self.cart.keys()
        artworks = Artwork.objects.filter(id__in=artwork_ids)
        
        cart = self.cart.copy()
        
        for artwork in artworks:
            cart[str(artwork.id)]['artwork'] = artwork
            
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item
        
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    def get_total_price(self):
        return sum(
            Decimal(item['total_price'] * item['quantity']) for item in self.cart.values()
        )
        
    def clear(self):
        ''' 
        Remove cart from session.
        '''
        del self.session[settings.CART_SESSION_ID]
        
        self.save()