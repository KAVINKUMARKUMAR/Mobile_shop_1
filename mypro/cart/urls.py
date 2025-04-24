from django.urls import path
from .views import viewCart, addtocart ,remFromCart

urlpatterns = [
    path('',viewCart, name='view_cart'),
    path('addcart/<int:product_id>/', addtocart , name='add_to_cart'),
    path('rem/<int:product_id>/', remFromCart, name='rem_from_cart')
]
