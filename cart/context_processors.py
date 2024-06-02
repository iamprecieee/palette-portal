from .cart import Cart


def cart(request):
    ''' 
    Context processor for persisting cart through all necessary templates
    '''
    return {'cart': Cart(request)} 


def show_subheader(request):
    return {'show_subheader': True}