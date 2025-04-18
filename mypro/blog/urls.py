from django.urls import path
from . import views

urlpatterns = [
    path('',views.homeview,name='home'),
    path('product/<int:pk>',views.Productdetial.as_view(),name='prod_detial'),
    path('product/add',views.AddProduct.as_view(),name='prod_add'),
]
