from django.urls import path
from . import views

from authentication.views import userlogin

urlpatterns = [
    path('',views.homeview,name='home'),
    path('product/<int:pk>',views.Productdetial.as_view(),name='prod_detial'),
    path('product/add',views.AddProduct.as_view(),name='prod_add'),
    path('product/edit/<int:pk>',views.EditProduct.as_view(),name ='edit_prod'),
    path('product/delete/<int:pk>',views.DeleteProduct.as_view(),name='del_prod'),
]
