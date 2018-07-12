from django.shortcuts import get_object_or_404
from products.models import Product

'''
products will not be stored in a database they will only be stored in the session while the shopper is logged in, when they log out the cart will be lost
'''

def cart_contents(request):
    """
    the cart contents will be available from any page while the shopper is logged in
    """
    
    cart = request.session.get('cart',{})
    cart_items =[]
    total = 0
    product_count=0
    # takes to things the id of the product and the quantity of the that product
    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        total += quantity * product.price
        product_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'product': product})
    
    #return a dictionary total:product count
    return{ 'cart_items': cart_items, 'total': total, 'product_count': product_count}