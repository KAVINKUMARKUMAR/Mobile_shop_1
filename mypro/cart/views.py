from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from blog.models import Product 
from .models import CartItem
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.shortcuts import get_list_or_404
# Create your views here.

@login_required
def viewCart(request):

    cartItem = CartItem.objects.filter(user = request.user)
    total_price = sum(item.product.price * item.quantity for item in cartItem)
    template = 'cart.html'

    context = {
        'items' : cartItem,
        'total' : total_price
    }

    return render(request,template,context)

def addtocart(request, product_id):
    this_product = Product.objects.get(id = product_id)

    cart_Item, created_at = CartItem.objects.get_or_create(product = this_product,user = request.user)
    cart_Item.quantity +=1

    cart_Item.save()

    return redirect('view_cart')

def remFromCart(request, product_id):
    
    this_cart_item = CartItem.objects.get(id = product_id)
    this_cart_item.delete()

    return redirect('view_cart')