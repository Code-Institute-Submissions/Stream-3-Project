from django.shortcuts import render
from .models import Product

# returns all products 
def all_products(request):
    # returns all products
    in_stock_products = Product.objects.all 
  
    # sends all products to products.html page
    return render(request, 'products.html', {"in_stock_products": in_stock_products})
     
