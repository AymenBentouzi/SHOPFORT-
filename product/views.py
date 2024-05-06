from django.shortcuts import render

# Create your views here.

from .models import Product


def product_list(request): 
    product_list = Product.objects.all()
    context = {'product_list' : product_list}
    return render(request, 'Product/product_list.html' , context)

def product_detail(request, id):
    product_detail = Product.objects.get(id=id)
    context = {'product_detail' : product_detail}
    return render(request, 'Product/product_detail.html' , context)
    
    


